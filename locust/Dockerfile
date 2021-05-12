FROM python:3.8

RUN mkdir /opt/locust/
WORKDIR /opt/locust/
ADD requirements.txt ./
ADD src ./src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --use-feature=2020-resolver

CMD locust -f src/locustfile.py