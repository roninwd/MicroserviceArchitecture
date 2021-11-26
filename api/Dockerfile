FROM golang:1.17.1-alpine

RUN mkdir /files

COPY . /files
WORKDIR /files

RUN go build -o /files/main main.go
EXPOSE 8000
ENTRYPOINT ["/files/main"]

