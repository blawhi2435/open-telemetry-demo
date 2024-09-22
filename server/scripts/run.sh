#!/bin/sh

# Run the client
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --logs_exporter otlp \
    --service_name server \
    uvicorn app.main:app --host 0.0.0.0 --port 8081