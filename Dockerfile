FROM python:3 

ENV PYTHONBUFFERED 1
WORKDIR /code

COPY reqirements.txt reqirements.txt
RUN pip install reqirements.txt

COPY . .

CMD ['python3', 'manage.py', 'runserver', '0.0.0.0:7000']