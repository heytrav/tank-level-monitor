FROM python:3-alpine

RUN apk update \
  && apk --no-cache add \
  moreutils 


RUN adduser -D defaultuser
USER defaultuser
WORKDIR /home/defaultuser
COPY json-convert.py .


