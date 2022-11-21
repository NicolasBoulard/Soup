FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app

RUN cd /app/docker &&\
    mv * ../ && cd .. &&\
    rm -rf /app/docker/
#ENTRYPOINT ["python3"]
RUN chmod +x /app/prestart.sh
CMD ["/app/prestart.sh"]
EXPOSE 8000