from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy

# ініціалізація Flask
app = Flask(__name__)

# Налаштування бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ініціалізація SQLAlchemy
db = SQLAlchemy(app)

# Модель для роботи з базою даних
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route("/api/v1/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
