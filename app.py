from flask import Flask, jsonify
from flask_restful import Api, Resource,request
import pickle
import json
from flask_cors import CORS
from functions import *

app = Flask(__name__)
CORS(app)



@app.route("/savePerson")
def hello_world():
    return f"<p>{train_classifier('fama')}</p>"




@app.route("/searchPerson")
def search():
    return f"<p>{predict('fama')}</p>"



# Cette liste contient la liste des noms de fichiers
search_data = get_xml_files()
print(search_data)

@app.route("/searchWord")
def searchWord():
    query = request.args.get('word')
    results = []
    if query:
        # Recherche de résultats correspondant à la requête
        print(search_data)
        for item in search_data:
            if query.lower() in item.lower():
                results.append(item)
    return results



if __name__ == "__main__":
    app.run()
