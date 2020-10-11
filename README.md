# Rest Backend for Organiz'R

![Python application](https://github.com/soft-r-evolutions/organiz_rest/workflows/Python%20application/badge.svg)

This project is made thanks to [Realpython tutorial](https://realpython.com/flask-connexion-rest-api/).


## Installation

### Installing virtual-env

On ubuntu

```
sudo apt install vitualenv
```

### Create environment

```
virtualenv --python=python3 venv
```

## Activate environment

```
source venv/bin/activate
```

## Install locally

```
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install flake8 black
pip install pytest pytest-cov

pip install flask
pip install connexion[swagger-ui]
```

## Linter

### Help formatting the code with black

Run black to help to fix linter issues. Warning must be done is separate commits for QA.

```
black organiz_rest
black tests
```

### Run the linter

Stop the build if Python syntax errors or undefined names

```
flake8 organiz_rest --exclude organiz_rest/__init__.py --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 tests --count --select=E9,F63,F7,F82 --show-source --statistics
```

Treats all errors as warnings

```
flake8 organiz_rest --exclude organiz_rest/__init__.py --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
flake8 tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## Run the tests

```
pytest --cov-config=.coveragerc --cov=organiz_rest --cov-report=html --cov-report=term --log-cli-level=6 tests
xdg-open htmlcov/index.html
```

## Run the tests

```
python organiz_rest/app.py
```

To check people:

```
xdg-open http://localhost:5000/api/people
```

Or to consult swagger ui:

```
xdg-open http://localhost:5000/api/ui
```


## Packaging

### Make a distributable package

```
python3 setup.py sdist
```

### Install local package

```
pip install path/to/file.tar.gz
```

## References

* [Python Application Layout](https://realpython.com/python-application-layouts/)
* [Semantic Versionning](https://semver.org/)

[Powered by PyProject Creator - MIT License](https://github.com/soft-r-evolutions/pyproject_creator)
