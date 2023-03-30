# gunicorn_config.py for Docker

# Listen to all the interfaces
bind = "0.0.0.0:80"

#certfile="/home/fullchain.pem"
#keyfile='/home/privkey.pem'

# Number of workers
workers = 5

# Set a large timeout if your embedding file is big as it may take a while to load the app
# You'll know that you have to increase the timeout if in error.log you see something like
#  [CRITICAL] WORKER TIMEOUT (pid:16) 
timeout = 60

threads = 2
worker_class = "sync"

# In Azure, there is a persistent volume in /home
accesslog = "/home/access.log"
errorlog = "/home/error.log"


