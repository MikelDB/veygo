FROM python:3.8-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt update

RUN apt install -y python-mysqldb default-libmysqlclient-dev libssl-dev build-essential python3-dev

RUN pip install --upgrade setuptools

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["server.py"]
