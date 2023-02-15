from flask import Flask, jsonify
from flask_restful import Api, Resource,request
import pickle
import json
from flask_cors import CORS
from functions import train_classifier,predict

app = Flask(__name__)
CORS(app)



@app.route("/savePerson")
def hello_world():
    return f"<p>{train_classifier('fama')}</p>"




@app.route("/searchPerson")
def search():
    return f"<p>{predict('fama')}</p>"

















if __name__ == "__main__":
    app.run()
