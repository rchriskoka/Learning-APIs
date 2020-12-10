FROM python:3.6-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src/app
COPY cashman ./cashman

RUN pipenv install

EXPOSE 5000
ENTRYPOINT ["bootstrap.sh"]
