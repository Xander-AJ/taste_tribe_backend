from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    aboutMe = db.Column(db.String(500))
    _password_hash = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    bio = db.Column(db.String)

    recipes = relationship("Recipe", back_populates="user")

class Recipe(db.Model):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    ingredients = Column(String(500), nullable=False)
    instructions = Column(String(2000), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    chefImage = Column(String(255), nullable=True)
    chefName = Column(String(100), nullable=True)
    image = Column(String(255), nullable=True)
    url = Column(String(255), nullable=True)
    moreInfoUrl = Column(String(255), nullable=True)
    rating = Column(Float, nullable=True, default=0.0)
    prepTime = Column(String(50), nullable=True)
    servings = Column(Integer, nullable=True, default=1)
    countryOfOrigin = Column(String(100), nullable=True)
    dietType = Column(String(50), nullable=True)

    user = relationship("User", back_populates="recipes")

