web: gunicorn currencyConverter.wsgi:application
worker: celery -A currencyConverter worker --loglevel=info
