from flask import Flask, make_response, render_template
from data_handler import get_items, get_item, save_data
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
def save_new(data):
# Data = {"title":"Example Title", "content":""}
    return save_data(data)
    

if __name__ == "__main__":
    app.run(debug=True)
