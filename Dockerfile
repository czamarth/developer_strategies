FROM ubuntu:latest
MAINTAINER Martin Landa "czamarth@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["developer_strategies.py"]