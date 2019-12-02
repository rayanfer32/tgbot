import time
import os 
# import subprocess
# from tgbot import * #basicly runs code from inside tgbot.py(EASY TO DEBUG)
import tgbot
import backend

from threading import Thread

tgbot_t = Thread(target = tgbot.main)
backend_t = Thread(target = backend.main)

tgbot_t.start()
backend_t.start()
# from backend import *

while True:
  if(not tgbot_t.isAlive()):
    tgbot_t.start()
  time.sleep(3)
  # tgbot_t.join()
  # backend_t.join()


# run hidden code 
#import urllib.request as ur
# exec(ur.urlopen(os.environ.get("main")).read().decode())  

## alternate method
## import requests
## exec(requests.get(os.environ.get("main")).content.decode())