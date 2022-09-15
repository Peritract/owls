from flask import Flask, render_template, abort

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
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/owls/", methods=["GET"])
def owls_index():
    return render_template("owls.html", owls=owls, title="Our Current Owls")

@app.route("/owls/<int:id>/", methods=["GET", "DELETE", "PATCH"])
def owls_show(id):
    matching_owls = [x for x in owls if x["id"] == id]
    if len(matching_owls) == 1:
        owl = matching_owls[0]
        return render_template("owl.html", owl=owl)
    else:
        abort(404)

@app.route("/owls/new/", methods=["GET", "POST"])
def owls_new():
    return "A form to make a new owl"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/400.html", error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template("errors/400.html", error=error)

@app.errorhandler(400)
def bad_request(error):
    return render_template("errors/400.html", error=error)

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("errors/405.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)