#!/bin/sh

# Run the client

    OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true \
    opentelemetry-instrument \
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --logs_exporter otlp \
    --service_name client \
    uvicorn app.main:app --host 0.0.0.0 --port 80