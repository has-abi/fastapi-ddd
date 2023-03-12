FROM tiangolo/uvicorn-gunicorn:python3.10-slim

RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
    netcat \
    && apt-get -q clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set env variables
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install pipenv
RUN pip install pipenv

# COPY python dependencies
COPY ./Pipfile /usr/src/app/Pipfile
COPY ./Pipfile.lock /usr/src/app/Pipfile.lock

# Install python dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Add app
COPY . /usr/src/app

EXPOSE 8000