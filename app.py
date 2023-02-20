import base64
from flask import Flask, jsonify
from flask_restful import Api, Resource,request
import pickle
import json
from flask_cors import CORS
from functions import *

import os
import os.path
from os import path

y = 0
def add_photo():
  global y
  y = y + 1
  
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



@app.route("/saveUser", methods=['POST'])
def saveUser():
     
     path_projet = 'C:\\Users\\ass_s\\Face_Recognition'
     data = request.get_json()
     nameUser = data.get('nameUser')
     photoUser = data.get('photoUser')
     # Set the path for the new directory
     directory = path_projet +'\\' + nameUser
   
     #Condition pour créer un directory
     if(path.isdir(directory) == False):
          # Use makedirs() to create the directory
         os.makedirs(directory)
         

     for x in photoUser:
        photo_data = base64.b64decode(x)
     
        add_photo();
    
        with open(directory+"/photo"+str(y)+".png", "wb") as file:
            file.write(photo_data)
    
     return f"Name: {nameUser}, Photo: {'saved'}"


@app.route("/searchUser", methods=['POST'])
def searchUser():
    path_projet = 'C:\\Users\\ass_s\\Face_Recognition'
    data = request.get_json()
    #nameUser = data.get('nameUser')
    photoInconnu = data.get('photoInconnu')
     # Set the path for the new directory
    directory = path_projet +'\\' + 'Searchs'
         #Condition pour créer un directory
    if(path.isdir(directory) == False):
          # Use makedirs() to create the directory
         os.makedirs(directory)
    
    photo_data = base64.b64decode(photoInconnu)
     
    
    with open(directory+"/inconnu.png", "wb") as file:
        file.write(photo_data)
        
    return f"Photo: {'success'}"
    

if __name__ == "__main__":
    app.run()
