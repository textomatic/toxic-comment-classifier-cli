install:
	pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
	python setup.py develop

lint:
	pylint --disable=R,C classify.py test_classify.py

format:
	black classify.py test_classify.py

test:
	python -m pytest -vv test_classify.py

all: install lint format test 