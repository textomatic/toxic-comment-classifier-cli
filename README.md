# toxic-comment-classifier-cli

[![GitHub Actions CI](https://github.com/textomatic/toxic-comment-classifier-cli/actions/workflows/main.yml/badge.svg)](https://github.com/textomatic/toxic-comment-classifier-cli/actions/workflows/main.yml)

## Description
This project is about creating a command line interface (CLI) tool for generating predictions from a pre-trained machine learning model and setting up Continuous Integration (CI) for the tool. The ML model being used is  [toxic-bert](https://huggingface.co/unitary/toxic-bert). The model is retrieved from HuggingFace and input text is passed to it to perform classification on whether toxicity exists. There are various labels of toxicity such as `toxic`, `insult`, `obscene`, `threat`, etc. If toxicity is detected, the label(s) and their corresponding score are returned.

## Setup
1. Clone the git repo to your local environment and change directory to it:
```bash
git clone https://github.com/textomatic/toxic-comment-classifier-cli.git`
cd toxic-comment-classifier-cli
```

2. Create a Python virtual environment and activate it:
```bash
python -m venv .venv/toxicity-classifier-cli
source .venv/toxicity-classifier-cli/bin/activate
```

3. Run the Make file:
```bash
make all
```

## Usage
Use the command `toxic_classify` and pass in your text for classification with the `--text` option:
```bash
toxic_classify --text "What a horrible person!"
```

And you should see the following results returned:
```bash
Classification complete!
--------------------------------------------------
   label    score
0  toxic  0.84842
```

If you would like to change the threshold score (default=0.5) for filtering results, pass in a custom value with the `--threshold` option:
```bash
toxic_classify --text "What a horrible person!" --threshold 0.1
```

And you should see the following results returned:
```bash
Classification complete!
--------------------------------------------------
    label     score
0   toxic  0.848420
1  insult  0.268856
```

If the threshold set is too high, no labels may be returned. The output in such cases will be `No toxicity detected!`.

## Continuous Integration
CI has been set up for this project and is done through GitHub Actions. The steps of the CI workflow are defined in this [YAML file](https://github.com/textomatic/toxic-comment-classifier-cli/blob/main/.github/workflows/main.yml). Whenever a change is pushed to repository, CI will be triggered and all the steps in the workflow will be performed to verify if the change is acceptable.

## Repository Structure

```
|-- .github
      |__ workflows
          |__ main.yml
|-- .gitignore
|-- Makefile
|-- README.md
|-- classify.py
|-- requirements.txt
|-- setup.py
|__ test_classify.py
```