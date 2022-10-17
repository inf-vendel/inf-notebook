from flask import Flask, make_response
from data_handler import get_items, get_item
from util import json_response
app = Flask(__name__)

@app.route('/')
def hello_geek():
    text = get_item("test_page")
    items = get_items()
    return f"<h1>It's working!</h1> \n {items[0]} {text}"

@app.route("/data")
@json_response
def load_pages():
    return get_items()

@app.route("/<page>")
@json_response
def load_page(page):
    return get_item(page)

if __name__ == "__main__":
    app.run(debug=True)
