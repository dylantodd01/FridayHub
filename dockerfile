FROM python:3.9
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./requirements.txt 
RUN pip3 install -r requirements.txt 
EXPOSE 8501
COPY . /app
WORKDIR /app
HEALTHCHECK CMD curl --fall https://localhost:8501/_stcore/health 
ENTRYPOINT [ "streamlit", "run hello.py" ]
CMD ["hello.py"]