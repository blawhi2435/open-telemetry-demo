#!/bin/sh

# Run the client
opentelemetry-instrument \
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --logs_exporter otlp \
    --service_name server \
    uvicorn app.main:app --host 0.0.0.0 --port 8081