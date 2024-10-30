# explore_cracow

#### 1. Usage, classic
```
Setup environment
 - python -m venv venv
 - source venv/bin/activate
 - pip install -r requirements.txt

Generate trip (5 monuments):
 - PYTHONPATH=. python cli/cli.py -n 5
```

#### 2. Usage, docker
```
 - docker build -t explore_cracow_cli .
 - docker run explore_cracow_cli cli/cli.py -n 3
```