# gunicorn_config.py for dev environment
bind = "127.0.0.1:8000"
workers = 4
threads = 2
worker_class = "sync"
accesslog = "./log/dev_access.log"
errorlog = "./log/dev_error.log"
# for testing cert
#certfile="./log/fullchain.pem"
#keyfile='./log/privkey.pem'
