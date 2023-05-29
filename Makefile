install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint --disable=R,C classify.py

format:
	black classify.py test_classify.py

test:
	python -m pytest -vv test_classify.py

all: install lint format test 