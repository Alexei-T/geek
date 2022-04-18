FROM golang:latest
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN go mod download && go build -o myapp_goland .
EXPOSE 8080
ENTRYPOINT [ "/app/myapp_goland" ]
