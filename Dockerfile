FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /explore_cracow

COPY ./requirements.txt /explore_cracow/requirements.txt
COPY ./static /explore_cracow/static
COPY ./shared /explore_cracow/shared
COPY ./cli /explore_cracow/cli
RUN pip install -r requirements.txt

ENV PYTHONPATH ./
ENTRYPOINT ["python"]

# from root directory:
#  docker build -t explore_cracow_cli .
#  docker run explore_cracow_cli cli/cli.py -n 3
