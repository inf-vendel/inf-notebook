# inf-notebook
A local webapp to create and read markdown files used for learning.
Flask server using dynamic html file, CSS and JavaScript.

---

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Use](#use)
* [Status](#status)
* [Upcoming features](#upcoming-features)

## General info
This is a fun project to have a simple application for creating and reading notes in markdown format. 
 
## Technologies
Project is created with:
* Pyhton 3.6.9
* Flask version: 2.0.2
* HTML5
* CSS3
* Python-Markdown version 3.3.7
* Javascript
* Bootstrap version 4.1.3
* SimpleMDE - Markdown Editor (https://github.com/sparksuite/simplemde-markdown-editor)

## Setup
There is a setup_venv.info on how to set up a virtual environment for the flask application.

Use the command `python app/server.py` to run the server on port 5000.

## Use
Put your `.md` files in the `app/data/` folder and the application will reload them with each request.

## Status
This project is currently under development.

## Upcoming features
* Create a markdown note in the webapp.
* Edit a markdown note in the webapp.
* Webdesign.
