import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


# -------------- Create instance of App ---- #
app = Flask(__name__)


# ---------------- App Configuration ------ #
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# -----------------Instance of MongoDB ----- #
mongo = PyMongo(app)


# ------------ View of Homepage Configuration --- #
@app.route("/")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
