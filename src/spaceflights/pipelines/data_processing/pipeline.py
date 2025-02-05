"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.10
"""


from kedro.pipeline import Pipeline, pipeline, node
from .nodes import (
    preprocess_comapanies,
    preprocess_shuttles,
    create_model_input_table)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_comapanies,  # Funções de nodes
            inputs="companies",
            outputs="preprocessed_companies",
            name="preprocess_companies_node"
        ),
        node(
            func=preprocess_shuttles,
            inputs="shuttles",
            outputs="preprocessed_shuttles",
            name="preprocess_shuttles_node"
        ),
        node(
            func=create_model_input_table,
            inputs=["preprocessed_shuttles",
                    "preprocessed_companies",
                    "reviews"],
            outputs="model_input_table",
            name="create_model_input_table_node"
        )
    ])
