from flask import Flask, render_template, Response
import prometheus_metrics
import logging
import os
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Ensure data directory exists
DATA_DIR = '/app/data'
os.makedirs(DATA_DIR, exist_ok=True)


def get_visit_count():
    count_file = os.path.join(DATA_DIR, 'visit_count.txt')
    try:
        with open(count_file, 'r') as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0


def increment_visit_count():
    count = get_visit_count() + 1
    count_file = os.path.join(DATA_DIR, 'visit_count.txt')
    with open(count_file, 'w') as f:
        f.write(str(count))
    return count


@app.route('/')
def home():
    visit_count = increment_visit_count()
    logger.info(f"Home page accessed - Total visits: {visit_count}")
    prometheus_metrics.page_views.labels(page='home').inc()
    return render_template('index.html', visit_count=visit_count)

# ... rest of the code remains the same ...
