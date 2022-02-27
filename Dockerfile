FROM python:3
WORKDIR /code
COPY requriements.txt /code/
RUN pip install -r requriements.txt
COPY . /code/
