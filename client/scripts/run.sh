#!/bin/sh

# Run the client
export OTEL_PYTHON_LOG_CORRELATION=true 

opentelemetry-instrument \
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --logs_exporter otlp \
    --service_name client \
    uvicorn app.main:app --host 0.0.0.0 --port 80