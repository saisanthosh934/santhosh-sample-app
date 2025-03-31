import time
from prometheus_client import Counter, Histogram, Gauge

# Metrics definitions
page_views = Counter(
    'page_views_total',
    'Total number of page views',
    ['page']
)

health_checks = Counter(
    'health_checks_total',
    'Total number of health checks'
)

metrics_requests = Counter(
    'metrics_requests_total',
    'Total number of metrics requests'
)

request_latency = Histogram(
    'http_request_latency_seconds',
    'HTTP request latency in seconds',
    ['endpoint']
)

app_uptime = Gauge(
    'app_uptime_seconds',
    'Application uptime in seconds'
)

# Update uptime metric
start_time = time.time()


def update_uptime():
    app_uptime.set(time.time() - start_time)
