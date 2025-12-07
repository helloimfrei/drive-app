from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()


class Brand(db.Model):
    __tablename__ = "brand"

    brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(50), nullable=False, unique=True)

    # Relationships
    accessories = db.relationship("Accessory", back_populates="brand")
    models = db.relationship("Model", back_populates="brand")


class Item(db.Model):
    __tablename__ = "item"

    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_quality = db.Column(
        Enum("poor", "used", "used like new", "brand new", name="item_quality_enum"),
        nullable=False,
    )

    # Relationships
    accessory = db.relationship("Accessory", back_populates="item", uselist=False)
    car = db.relationship("Car", back_populates="item", uselist=False)
    listings = db.relationship("Listing", back_populates="item")


class Accessory(db.Model):
    __tablename__ = "accessory"

    item_id = db.Column(db.Integer, db.ForeignKey("item.item_id"), primary_key=True)
    access_descript = db.Column(db.String(255), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey("brand.brand_id"), nullable=True)

    # Relationships
    item = db.relationship("Item", back_populates="accessory")
    brand = db.relationship("Brand", back_populates="accessories")


class Model(db.Model):
    __tablename__ = "model"

    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_id = db.Column(db.Integer, db.ForeignKey("brand.brand_id"), nullable=False)
    model_name = db.Column(db.String(50), nullable=False)
    model_year = db.Column(
        db.SmallInteger, nullable=False
    )  # YEAR type maps to SmallInteger
    model_trim = db.Column(db.String(50), nullable=True)
    model_color = db.Column(db.String(30), nullable=True)

    __table_args__ = (
        db.UniqueConstraint(
            "brand_id", "model_name", "model_year", "model_trim", name="uq_model"
        ),
        db.Index("idx_model_brand_name", "brand_id", "model_name"),
    )

    # Relationships
    brand = db.relationship("Brand", back_populates="models")
    cars = db.relationship("Car", back_populates="model")


class Car(db.Model):
    __tablename__ = "car"

    item_id = db.Column(db.Integer, db.ForeignKey("item.item_id"), primary_key=True)
    car_vin = db.Column(db.String(17), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey("model.model_id"), nullable=True)

    # Relationships
    item = db.relationship("Item", back_populates="car")
    model = db.relationship("Model", back_populates="cars")


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_fname = db.Column(db.String(50), nullable=False)
    user_lname = db.Column(db.String(50), nullable=False)
    user_init = db.Column(db.CHAR(1), nullable=True)
    user_password = db.Column(db.String(255), nullable=False)
    user_dob = db.Column(db.Date, nullable=True)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    user_phone = db.Column(db.String(15), nullable=True)

    # Relationships
    listings = db.relationship(
        "Listing", back_populates="seller", foreign_keys="Listing.seller_id"
    )
    purchases = db.relationship("Purchase", back_populates="buyer")


class Listing(db.Model):
    __tablename__ = "listing"

    listing_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.item_id"), nullable=True)
    listing_location = db.Column(db.String(255), nullable=False)
    listing_price = db.Column(db.Numeric(10, 2), nullable=False)
    listing_status = db.Column(db.String(50), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=True)

    # Relationships
    item = db.relationship("Item", back_populates="listings")
    seller = db.relationship(
        "User", back_populates="listings", foreign_keys=[seller_id]
    )
    purchases = db.relationship("Purchase", back_populates="listing")


class Purchase(db.Model):
    __tablename__ = "purchase"

    purchase_id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.Date, nullable=False)
    listing_id = db.Column(
        db.Integer, db.ForeignKey("listing.listing_id"), nullable=True
    )
    purchase_price = db.Column(db.Numeric(10, 2), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=True)

    # Relationships
    buyer = db.relationship("User", back_populates="purchases")
    listing = db.relationship("Listing", back_populates="purchases")
