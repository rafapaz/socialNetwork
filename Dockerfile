FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y libsqlite3-dev
RUN pip install -U pip setuptools
ADD . /app/
RUN pip install -r /app/requirements.txt
EXPOSE 8000
ENTRYPOINT [ "/bin/sh" ]
CMD [ "/app/run_web.sh" ]