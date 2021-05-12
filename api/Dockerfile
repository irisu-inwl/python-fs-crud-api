FROM python:3.8

RUN mkdir /opt/crud-api/
WORKDIR /opt/crud-api/
ADD requirements.txt ./
ADD uwsgi.ini ./
ADD src ./src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --use-feature=2020-resolver

RUN useradd -m -u 1000 app 
RUN chown -R app:app /opt/crud-api/
USER app

CMD uwsgi --ini uwsgi.ini