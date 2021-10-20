# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/TornadoApp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/TornadoApp/entrypoint.sh"]