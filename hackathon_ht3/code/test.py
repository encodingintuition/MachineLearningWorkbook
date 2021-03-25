# imports
from flask import Flask, Response, request, render_template, jsonify
import numpy as np
import pickle

# initialize the flask app
app = Flask("myApp")

# route 1: hello world
# return a simple string
@app.route("/")
def home():
    return "Hello, DSI! You Rock!!!!"


# route 2: return a 'web page'
# return some hard-coded html
name = "Jeff"

x = (5 * 4 - 2)


@app.route("/hc_page")
def hc_page():
    return """
        <html>
            <body>
                <h1>This is a hard-coded page!</h1>
                <p> Here is some hard-coded content. {name} Isn't it lovely? {x} 🎉</p>
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


# route 4: show a form to the user
# use flask's render_template function to display an html page
@app.route("/form")
def form():
    return render_template("form.html")


# route 5: accept the form submission and do something fancy with it
# manipulate data into a format that we pass to our model
@app.route("/submit")
def make_predictions():

    # load in the form data from the incoming request
    user_input = request.args

    X_test = np.array(
        [
            int(user_input["OverallQual"]),
            int(user_input["FullBath"]),
            int(user_input["GarageArea"]),
            int(user_input["LotArea"]),
        ]
    ).reshape(1, -1)

    model = pickle.load(open("assets/model.p", "rb"))
    pred = model.predict(X_test)
    pred = pred[0]

    return render_template("results.html", prediction=pred)
    # return jsonify({"prediction": pred})


# Call app.run(debug=True) when python script is called
if __name__ == "__main__":
    app.run(debug=True)