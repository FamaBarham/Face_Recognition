import base64
from flask import Flask, jsonify
from flask_restful import Api, Resource,request
import pickle
import json
from flask_cors import CORS
import os
import os.path
from os import path

x = 0
def add_photo():
  global x
  x = x + 1
  
app = Flask(__name__)
CORS(app)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


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
         

    
     photo_data = base64.b64decode(photoUser)
     add_photo()
    
     with open(directory+"/photo"+str(x)+".png", "wb") as file:
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
