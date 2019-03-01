FROM ubuntu:18.04
COPY . /app
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3.6 python3-setuptools software-properties-common
RUN add-apt-repository universe
RUN apt-get update
RUN apt-get install -y libffi-dev libxslt-dev
RUN apt-get install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libcairo2 python3-cairo python3-pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=azgar
ENV LANG=C.UTF-8
ENTRYPOINT flask run --host 0.0.0.0