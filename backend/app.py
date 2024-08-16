from flask import Flask, jsonify
from backend import app, db, bcrypt
from backend.models import User, Recipe

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Recipe API"})

if __name__ == "__main__":
    app.run(debug=True)
