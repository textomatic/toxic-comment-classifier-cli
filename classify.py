import click
from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")


def classify_text(text):
    classifier = pipeline(
        task='text-classification',
        model='unitary/toxic-bert',
        tokenizer='bert-base-uncased',
        function_to_apply='sigmoid',
        top_k=None
    )
    result = classifier(text)
    click.echo('Classification complete!')
    click.echo('-'*50)
    return result[0]


@click.command()
@click.option('--text')
def main(text):
    click.echo(classify_text(text))