import click
import pandas as pd
from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")


def classify_text(text, threshold):
    """
    Loads the classifier model and performs classification on the given piece of text to detect toxicity within it. Classification result is returned as a Pandas DataFrame showing the toxic labels and their corresponding scores. A default threshold score of `0.5` is used for filtering out non-relevant results. If result is empty, an informative string is returned instead.

    Args:
        text(str): String for toxicity classification.
        threshold(float): Threshold to apply for filtering classification results.
    
    Returns:
        final_df_result(pd.DataFrame or str): Result of classification.
    """
    classifier = pipeline(
        task="text-classification",
        model="unitary/toxic-bert",
        tokenizer="bert-base-uncased",
        function_to_apply="sigmoid",
        top_k=None,
    )
    result = classifier(text)
    df_result = pd.DataFrame(result[0])
    final_df_result = df_result[df_result["score"] >= threshold]
    if len(final_df_result) == 0:
        final_df_result = "No toxicity detected!"
    return final_df_result


@click.command()
@click.option("--text")
@click.option("--threshold", default=0.5)
def main(text, threshold):
    """
    Main driver function. Accepts a string as input and performs classification on it to detect presence of toxicity.
    Result of classification is printed to standard output through `click.echo()`.

    Args:
        text(str): Target string for toxicity classification
        threshold(float): Threshold to apply for filtering classification results. Defaults to `0.5`, i.e. any label with a score below `0.5` is excluded.

    Return:
        None
    """
    result = classify_text(text, threshold)
    click.echo("Classification complete!")
    click.echo("-" * 50)
    click.echo(result)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
