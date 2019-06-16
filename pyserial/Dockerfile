FROM python:3-alpine

RUN pip install pyserial
WORKDIR /var/lib/
RUN apk update \
  && apk --no-cache add --virtual native-deps \
  git \
  && git clone https://github.com/pyserial/pyserial.git \
  && apk del native-deps

WORKDIR /var/lib/pyserial/examples
