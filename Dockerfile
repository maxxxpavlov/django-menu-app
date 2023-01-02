FROM python:3.11.1-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "manage.py", "runserver" ]