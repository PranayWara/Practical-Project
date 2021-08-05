FROM python:latest
RUN apt update
RUN apt install python3-pip -y
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5002
ENTRYPOINT ["python","app.py"]