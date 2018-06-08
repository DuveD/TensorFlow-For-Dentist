#!/usr/bin/python

from pathlib import Path
from PIL import Image
from os.path import basename
import os

baseFolder = "tf_files"

originalImagesPath = baseFolder+"/originalImages"

newImagePath = baseFolder+"/newImages"

def editPhotos():
    # Eliminamos fotos si las hay
    if (os.path.exists(newImagePath)):
        print("Deleting images...")
        for dirname in os.listdir(newImagePath):
            for filename in os.listdir(newImagePath+"/"+dirname):
                os.remove(newImagePath+"/"+dirname+"/"+filename)
        print("...deleted")

    print("Checking for "+newImagePath+" folder...")
    if (not os.path.exists(newImagePath)):
        os.mkdir(newImagePath)
        print("...created!")

    print("Checking for images in original folder...")
    if (not os.path.exists(originalImagesPath)):
        tf.logging.error("Original folder '" + image_dir + "' not found.")
    for dirname in os.listdir(originalImagesPath):

        print("Checking for "+newImagePath+"/"+dirname+" folder...")
        if (not os.path.exists(newImagePath+"/"+dirname)):
            os.mkdir(newImagePath+"/"+dirname)
            print("...created!")

        print("Checking for images into "+newImagePath+"/"+dirname+" original folder...")
        for filename in os.listdir(originalImagesPath+"/"+dirname):
            image = Image.open(originalImagesPath+"/"+dirname+"/"+filename)
            print("Saving "+newImagePath+"/"+dirname+"/"+filename)
            transformAndSave(dirname, filename, image)

def transformAndSave(dirname, filename, image):
    # Modificamos las fotos y las guardamos
    degrees = 0
    while (degrees < 360):
        newImage = image.rotate(degrees, expand=True)
        print("Saving "+newImagePath+"/"+dirname+"/"+basename(filename)+str(degrees)+".jpeg")
        newImage.save(newImagePath+"/"+dirname+"/"+basename(filename)+str(degrees)+".jpeg")
        degrees = degrees + 30
