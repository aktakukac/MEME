# MEME GENERATOR

Udacity Intermediate Python Nanodegree <br>
Project 2 <br>
Mihaly Garamvolgyi <br>
2022-09-27

## Overview
Generate motivational memes that are images with quotes and author signatures. <br>
User can supply their own image and quotes or can be generated randomly from the apps image and qoute directory. <br>
Implementation is twofold: a CLI driven usage or through a web browser (Flask implementation)

## Setting up and running
1. Go to directory
2. Create venv `python -m venv venv`
3. Activate venv source `venv/bin/activate` or `.\venv\Scripts\activate.bat` on Windows
4. Install requirements `pip install -r requirements.txt`

### prerequisities
* Python 3.10.5
* pdftotext CLI application
* required packages are listed in requirements.txt
* Flask
* web browser

### command line
Run the `meme.py` with the following optional parameters:
* `path` - original image
* `body` - qoute text
* `author` - quote author

### flask app
Export app as a FLASK_APP and navigate to the ip address with a browser.
1. navigate to the project directory 
2. run `export FLASK_APP=app.py` or `set FLASK_APP=app.py` on Windows
3. run `flask run --host 0.0.0.0 --port 3000 --reload`
4. Get the IP adress and port printed by Flask
5. Access with a web browser

## Sub modules
### Quote Engine
Module for ingesting qoutes from a number of different file types. Individual ingestors are developed for CSV, TXT, DOCX and PDF files and are packaged into an ingestor module.

### Meme Generator
Module for generating the memes. Uses python Pillow library for resizing and captioning images. 