# imports necessary tools from flask
from flask import Blueprint, render_template, request
from utils import fetch_restaurants

# creates blueprint for views
views = Blueprint(__name__, "views")

@views.route("/", methods=["GET"])
def home():
    postcode = request.args.get("postcode") # gets postcode
    
    # inisilises empty restaurants and messege
    restaurants = []
    message = None

    # gets restauransts for the input postcode
    if postcode:
        restaurants = fetch_restaurants(postcode)

        # error message if no restaurants or invalid postcode
        if not restaurants:
            message = f"{postcode} is not a valid UK postcode or has no restaurants."

    # connects backend to HTML frontend, displaying content based on user search
    return render_template(
        "index.html",
        restaurants=restaurants,
        postcode=postcode,
        message=message
    )