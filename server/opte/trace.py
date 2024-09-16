from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

# 設置 TracerProvider
provider = TracerProvider()

# 配置 OTLPSpanExporter
otlp_exporter = OTLPSpanExporter()

# 設置 BatchSpanProcessor 並添加 OTLPExporter
processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)

# 設置全局默認 TracerProvider
trace.set_tracer_provider(provider)

# 創建 Tracer
tracer = trace.get_tracer("my.tracer.name")
