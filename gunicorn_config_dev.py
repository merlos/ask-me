# gunicorn_config.py for dev environment
bind = "127.0.0.1:8000"
workers = 4
threads = 2
worker_class = "sync"
accesslog = "./log/ask_me_access.log"
errorlog = "./log/ask_me_error.log"