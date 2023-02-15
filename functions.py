import numpy as np
from PIL import Image
import os
import cv2 as cv

def train_classifier(name):
    path = os.path.join(os.getcwd()+"/"+name+"/")
    faces = []
    ids = []
    labels = []
    pictures = {}

    for root,dirs,files in os.walk(path):
            pictures = files

    for pic in pictures :

            imgpath = path+pic
            img = Image.open(imgpath).convert('L')
            imageNp = np.array(img, 'uint8')
            faces.append(imageNp)
            ids.append(1)

    labels = np.array(ids)

    # Train and save classifier
    clf = cv.face.LBPHFaceRecognizer_create()
    clf.train(faces, labels)
    clf.write("ModelsMachineLearning/"+name+"_classifier.xml")
    # SUPPRESSION DU DOSSIER DES IMAGES(EN FAIRE UNE FONCTION ET L'APPELLER)
    return pictures


def predict(name):
    classifierPath = os.path.join(os.getcwd()+"/ModelsMachineLearning/"+name+"_classifier.xml")
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read(classifierPath)
    imgpath = os.path.join(os.getcwd()+"/searchs/"+name+".jpeg")
    img = Image.open(imgpath).convert('L')
    imageNp = np.array(img, 'uint8')
    id,confidence = recognizer.predict(imageNp)
    return confidence