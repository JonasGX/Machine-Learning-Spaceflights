"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.10
"""

import pandas as pd


def _is_true(x: pd.Series) -> pd.Series:
    data = x == "t"
    return data


def _parse_percent(x: pd.Series) -> pd.Series:
    data = x.str.replace("%", "").astype(float)
    return data


def _parse_money(x: pd.Series) -> pd.Series:
    data = x.str.replace(",", "").str.replace("$", "").astype(float)
    return data


def preprocess_comapanies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Estamos alterando as colunas e passando a função responsável por 
    transformar os valores f e t em False e True
    """
    df['iata_approved'] = _is_true(df['iata_approved'])

    """
    Estamos alterando as colunas e passando a função responsável por retirar
    o simbolo de $ e o de %
    """
    df['company_rating'] = _parse_percent(df['company_rating'])

    return df


def preprocess_shuttles(df: pd.DataFrame) -> pd.DataFrame:
    """
    Estamos alterando as colunas e passando a função responsável por retirar
    o simbolo de $ e o de %
    """

    df['d_check_complete'] = _is_true(df['d_check_complete'])
    df['moon_clearance_complete'] = _is_true(df['moon_clearance_complete'])
    df['price'] = _parse_money(df['price'])

    return df


def create_model_input_table(
        shuttles: pd.DataFrame,
        companies: pd.DataFrame,
        reviews: pd.DataFrame
        ) -> pd.DataFrame:
    rated_shuttles = shuttles.merge(reviews,
                                    left_on="id",
                                    right_on="shuttle_id")
    model_input_table = rated_shuttles.merge(companies,
                                             left_on="company_id",
                                             right_on="id")

    return model_input_table.dropna()
