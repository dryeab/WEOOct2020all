import pickle
from flask import Flask, request

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))


@app.route("/", methods=["POST"])
def index():
    body = request.get_json()
    return "Hello World"
