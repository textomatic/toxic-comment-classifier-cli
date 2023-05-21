from setuptools import setup, find_packages

with open('requirements.txt', 'r') as req_file:
    requirements = [line for line in req_file.read().split('\n')]

setup(
    name='toxicity_classifier',
    description='A Python CLI tool to classify toxic comments using the toxic-bert model', 
    packages=find_packages(),
    author='Shen Juin Lee',
    entry_points="""
    [console_scripts] classify=classify.main:main
    """,
    install_requires=requirements, 
    version='0.0.1', 
    url='https://github.com/textomatic/toxic-comment-classifier-cli'
)