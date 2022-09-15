from flask import Flask, render_template

app = Flask(__name__)

owls = [
    {
        "id": 0,
        "name": "Archimedes",
        "species": "owl",
        "favourite_colour": "blue"
    },
    {
        "id": 1,
        "name": "Bertrand",
        "species": "owl",
        "favourite_colour": "teal"
    },
    {
        "id": 2,
        "name": "Jack",
        "species": "owl",
        "favourite_colour": "purple"
    },
    {
        "id": 3,
        "name": "Circe",
        "species": "owl",
        "favourite_colour": "green"
    }
]

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the Owl House!"

@app.route("/about", methods=["GET"])
def about():
    return "Owl About Owls"

@app.route("/owls/", methods=["GET"])
def owls_index():
    return render_template("owls.html")

@app.route("/owls/<int:id>/", methods=["GET", "DELETE", "PATCH"])
def owls_show(id):
    return "An individual owl"

@app.route("/owls/new/", methods=["GET", "POST"])
def owls_new():
    return "A form to make a new owl"

@app.errorhandler(404)
def page_not_found(error):
    return f"404: page not found"

@app.errorhandler(500)
def server_error(error):
    return "500: server error"

@app.errorhandler(400)
def bad_request(error):
    return "400: bad request"

if __name__ == "__main__":
    app.run(debug=True)