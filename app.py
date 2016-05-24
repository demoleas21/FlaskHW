"""Flask Hello World"""

"""import the Flask class from the flask package"""
from flask import Flask

"""create the application object"""
app = Flask(__name__)

"""error handling"""
app.config["DEBUG"] = True

"""use decorators to link the function to a url and define a view using a function"""
@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!?!?!?"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"

"""dynamic route that accepts slashes"""
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "andrew":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404

"""start the development server using the run() method"""
if __name__ == "__main__":
    app.run()

