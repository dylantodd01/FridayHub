FROM python:3.9

RUN apt-get update
RUN apt-get install -y --reinstall ca-certificates

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["./hello.py"]