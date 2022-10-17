from flask import Flask
from data_handler import get_items, get_item
app = Flask(__name__)

@app.route('/')
def hello_geek():
    text = get_item("test_page")
    items = get_items()
    return f"<h1>It's working!</h1> \n {items[0]} {text}"


if __name__ == "__main__":
    app.run(debug=True)
