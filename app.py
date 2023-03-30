from flask import Flask
from s     import api1

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
  return api1()
if __name__ == '__main__':
    app.run(debug=True)
