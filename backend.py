
from flask import Flask
import os
app = Flask(__name__, static_folder='.', root_path='/home/runner')

@app.route('/')
def root():
    return app.send_static_file('./log.txt')

# if __name__ == '__main__':
def main():
  app.run(host='0.0.0.0', port='3000')

