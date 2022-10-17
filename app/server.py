from flask import Flask
from data_handler import get_items
app = Flask(__name__)

@app.route('/')
def hello_geek():
    items = get_items()
    return f"<h1>It's working!</h1> \n {items[0]}"


if __name__ == "__main__":
    app.run(debug=True)
