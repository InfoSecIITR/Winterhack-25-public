# Build the application from source
FROM golang:1.22 AS build-stage

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY ./cmd ./cmd
COPY ./routes ./routes
COPY ./static ./static
COPY ./utils ./utils

RUN CGO_ENABLED=0 GOOS=linux go build -o /challenge ./cmd

# Run the tests in the container
FROM build-stage AS run-test-stage
RUN go test -v ./pkg/helper

# Deploy the application binary into a lean image
FROM alpine:latest AS build-release-stage

WORKDIR /app

COPY --from=build-stage /challenge ./challenge

COPY ./keys ./keys
COPY ./templates ./templates
COPY ./static ./static

RUN adduser -D nonroot
RUN chown nonroot:nonroot ./
USER nonroot

CMD ["./challenge"]