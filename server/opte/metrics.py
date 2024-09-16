from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

# 設定 OTLPMetricExporter，這裡的 url 是 OpenTelemetry Collector 的地址
metric_exporter = OTLPMetricExporter()

# 使用 OTLPMetricExporter 來初始化 PeriodicExportingMetricReader
metric_reader = PeriodicExportingMetricReader(metric_exporter)

# 設定 MeterProvider 並設置 MetricReader
provider = MeterProvider(metric_readers=[metric_reader])

# 設置全局默認的 MeterProvider
metrics.set_meter_provider(provider)

# 從全局 MeterProvider 創建 Meter
meter = metrics.get_meter("my.meter.name")


cpu_usage_counter = meter.create_counter(
    "cpu_usage_seconds_total",
    description="Total CPU time used by the application"
)

memory_usage_gauge = meter.create_up_down_counter(
    "memory_usage_bytes",
    description="Memory usage in bytes"
)

storage_usage_gauge = meter.create_up_down_counter(
    "storage_usage_bytes",
    description="Storage usage in bytes"
)