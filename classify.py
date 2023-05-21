import click
from transformers import pipeline


def classify_text(text):
    classifier = pipeline(model="unitary/toxic-bert")
    result = classifier(text)
    click.echo('Classification complete!')
    click.echo('-'*50)
    return result


@click.command()
@click.option('--text')
def main(text):
    click.echo(classify_text(text))