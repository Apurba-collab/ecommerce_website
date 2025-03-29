from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce"
)
cursor = db.cursor()

@app.route("/wishlist", methods=["POST"])
def add_to_wishlist():
    data = request.json
    user_id = data.get("user_id")
    product_name = data.get("product_name")
    product_img = data.get("product_img")
    product_price = data.get("product_price")

    cursor.execute("INSERT INTO wishlist (user_id, product_name, product_img, product_price) VALUES (%s, %s, %s, %s)",
                   (user_id, product_name, product_img, product_price))
    db.commit()
    return jsonify({"message": "Added to wishlist!"})

@app.route("/wishlist/<int:user_id>", methods=["GET"])
def get_wishlist(user_id):
    cursor.execute("SELECT product_name, product_img, product_price FROM wishlist WHERE user_id = %s", (user_id,))
    wishlist_items = cursor.fetchall()
    return jsonify(wishlist_items)
