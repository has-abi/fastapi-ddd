FROM python:3.10

RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
    netcat \
    && apt-get -q clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"


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

# run server
CMD ["./entrypoint.sh"]