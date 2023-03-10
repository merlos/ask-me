# gunicorn_config.py for Docker
bind = "0.0.0.0:8000"
workers = 4
threads = 2
worker_class = "sync"
accesslog = "/home/access.log"
errorlog = "/home/error.log"