FROM alpine:latest
RUN apk add --update python python-dev gfortran py-pip build-base py-numpy
COPY flops.py /
COPY ep.sh /
ENTRYPOINT ["/ep.sh"]
