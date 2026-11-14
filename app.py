
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Margherita Pizza", "price": 199},
    {"id": 2, "name": "Farmhouse Pizza", "price": 299},
    {"id": 3, "name": "Peppy Paneer Pizza", "price": 349},
    {"id": 4, "name": "Veg Extravaganza", "price": 399},
    {"id": 5, "name": "Cheese Burst Pizza", "price": 449},
    {"id": 6, "name": "Chicken Dominator", "price": 499}
]

cart = []

@app.route("/")
def home():
    total = sum(item["price"] * item["quantity"] for item in cart)
    return render_template("index.html", menu=menu,
                           cart=cart, total=total)

@app.route("/add/<int:pizza_id>")
def add_to_cart(pizza_id):
    pizza = next((p for p in menu if p["id"] == pizza_id), None)

    if pizza:
        existing = next(
            (item for item in cart if item["id"] == pizza_id), None
        )

        if existing:
            existing["quantity"] += 1
        else:
            cart.append({
                **pizza,
                "quantity": 1
            })

    return redirect(url_for("home"))

@app.route("/remove/<int:pizza_id>")
def remove_from_cart(pizza_id):
    global cart
    cart = [item for item in cart if item["id"] != pizza_id]
    return redirect(url_for("home"))

@app.route("/order", methods=["POST"])
def place_order():
    global cart

    if not cart:
        return redirect(url_for("home"))

    customer = request.form.get("customer")
    address = request.form.get("address")

    total = sum(item["price"] * item["quantity"] for item in cart)

    order_details = {
        "customer": customer,
        "address": address,
        "total": total
    }

    cart = []

    return f"""
    <h1>Order Placed Successfully!</h1>
    <h3>Thank you, {customer}!</h3>
    <p>Delivery Address: {address}</p>
    <h2>Total Amount: Rs. {total}</h2>
    <a href="/">Back to Home</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
