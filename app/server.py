from urllib import request
from flask import Flask, make_response, render_template, request, redirect, flash
from data_handler import get_items, get_item, save_data
from util import json_response
import os
app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def index():
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

@app.route("/save_new", methods=["GET", "POST"])
def save_new():
    # Data = {"title":"Example Title", "content":""}
    if request.method == "POST":
        data = request.form.to_dict()
        title = data['title']
        content = data['input']
        print(data)
        result = save_data(data)
        flash(result['text'], result['type'])
        return redirect('/')
    else:
        return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=True)
