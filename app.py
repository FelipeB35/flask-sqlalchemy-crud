from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

if "__main__" == __name__:
  app.run(debug=True)

