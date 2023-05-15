FROM python:3.8-slim AS base

USER root
RUN apt-get update\
    && apt-get install curl -y

RUN apt-get update && apt-get -y install cron

FROM base AS exposing

EXPOSE 5000 5001

FROM exposing AS poetry-builder 

RUN pip install poetry==1.2.0

COPY . /api_app
WORKDIR /api_app

RUN poetry config virtualenvs.create false
RUN poetry install

FROM poetry-builder as nginx-settings

USER root
RUN chmod a+x run.sh

CMD ["./run.sh", "-v"]
