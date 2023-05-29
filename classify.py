import click
import pandas as pd
from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")


@click.command()
@click.option("--text")
def classify_text(text):
    classifier = pipeline(
        task="text-classification",
        model="unitary/toxic-bert",
        tokenizer="bert-base-uncased",
        function_to_apply="sigmoid",
        top_k=None,
    )
    result = classifier(text)
    df_result = pd.DataFrame(result[0])
    final_df_result = df_result[df_result['score'] >= 0.5]
    click.echo("Classification complete!")
    click.echo("-" * 50)
    click.echo(final_df_result)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    classify_text()
