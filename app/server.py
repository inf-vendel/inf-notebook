from flask import Flask, make_response, render_template
from data_handler import get_items, get_item
from util import json_response
app = Flask(__name__)

@app.route('/')
def hello_geek():
    text = get_item("test_page")
    items = get_items()
    return render_template("index.html")

@app.route("/data")
@json_response
def load_pages():
    return get_items()

@app.route("/<page>")
@json_response
def load_page(page):
    return get_item(page)

@app.route("/save<data>")
def save_data(data):
# Move this to data handler.
# Data = {"title":"Example Title", "content":""}
    filename = data["title"] 
    if filename in  get_tiems():
        return {"type":"error", "text":"Filename already taken."}
    with open(filename + ".md", "x", encoding = 'utf-8') as file:
        file.write(data["content"])
    

if __name__ == "__main__":
    app.run(debug=True)
