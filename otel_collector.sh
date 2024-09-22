#!/bin/sh

docker run -p 4317:4317 -p 4318:4318 \
    -v ./otel-collector-config.yaml:/etc/otel-collector-config.yaml \
    otel/opentelemetry-collector:latest \
    --config=/etc/otel-collector-config.yaml 