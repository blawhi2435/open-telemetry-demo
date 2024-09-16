from opentelemetry import trace
from fastapi import FastAPI
import psutil
from app.routers import order
from opte.metrics import cpu_usage_counter, memory_usage_gauge, storage_usage_gauge

# 初始化 FastAPI 儀表板時選擇性地禁用
app = FastAPI()

app.include_router(order.router, prefix="/server")

cpu_time = psutil.cpu_times().user
cpu_usage_counter.add(cpu_time)

# 獲取內存使用情況
memory_info = psutil.virtual_memory()
memory_usage_gauge.add(memory_info.used)

# 獲取存儲使用情況
storage_info = psutil.disk_usage('/')
storage_usage_gauge.add(storage_info.used)