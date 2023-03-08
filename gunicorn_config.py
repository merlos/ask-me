# gunicorn_config.py
bind = "127.0.0.1:8000"
workers = 4
threads = 2
worker_class = "sync"
accesslog = "./log/access.log"
errorlog = "./log/error.log"