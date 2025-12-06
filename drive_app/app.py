from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Listing(db.Model):
    __tablename__ = 'listing' 
    listing_id = db.Column(db.Integer, primary_key=True)
    listing_location = db.Column(db.String(200))
    listing_price = db.Column(db.Float)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/listing')
def show_listing():
    rows = Listing.query.all()
    return render_template("listing.html", listings=rows)


if __name__ == '__main__':
    app.run(debug=True)
