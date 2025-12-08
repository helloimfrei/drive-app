from flask import Flask, render_template
from dotenv import load_dotenv

from models import db, Listing
import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/listing")
def show_listing():
    rows = Listing.query.all()
    return render_template("listing.html", listings=rows)


@app.route("/listing/<int:listing_id>")
def listing_detail(listing_id):
    # get_or_404 returns a 404 page if not found
    listing = Listing.query.get_or_404(listing_id)
    return render_template("listing_detail.html", listing=listing)


if __name__ == "__main__":
    app.run(debug=True)
