# imports
from flask import Flask, Response, request, render_template, jsonify
import numpy as np


app = Flask("myApp")

# route 1: hello world
# return a simple string
@app.route("/")
def home():
    return "Hello, DSI! You Rock!!!!"

# sd
name = "Jeff"


@app.route("/hc_page")
def hc_page():
    return """
        <html>
            <body>
                <h1>This is a hard-coded page!</h1>
                <p> Here is some hard-coded content. {name} Isn't it lovely? 🎉</p>
            </body>
        </html>
    """

# route 3: return some data
# create some data to return as json
# use flask's jsonify function to return the data as well as a 200 status code
@app.route("/hc_page.json")
def json():
    best_stuff = {
        "Thanksgiving Food": "sweet potatoes",
        "sandwich": "Basil Something",
        "movie": "Zoolander",
    }
    return jsonify(best_stuff), 200


# Call app.run(debug=True) when python script is called
if __name__ == "__main__":
    app.run(debug=True)