#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Data to be stored
products = [
    {
        "id": 1,
        "name": "Fashion Natural Looking Straight Wraparound Ponytail Extension",
        "price": 200,
        "description": "The kinky straight wrap around ponytail blends perfectly with your natural hair...",
        "image": "https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/16/769033/2.jpg?1906",
    },
    {
        "id": 2,
        "name": "Afro Bun Ponytail Hair Extension SMALL+ Free Free Gift",
        "price": 200,
        "description": "Material: Heat Resistant Synthetic Drawstring, not Shiny...",
        "image": "https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/02/504755/1.jpg?7224",
    },
    {
        "id": 3,
        "name": "Fashion Curly Ponytail With Drawstring + FREE GIFT",
        "price": 200,
        "description": "Baby Curl Ponytail with Drawstring is designed for ladies that are willing to make classy fashion statement...",
        "image": "https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/81/815985/1.jpg?2659",
    },
    {
        "id": 4,
        "name": "Fashion Long Straight Ponytaill Hair Extension",
        "price": 200,
        "description": "The kinky straight wrap around ponytail blends perfectly with your natural hair...",
        "image": "https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/57/130835/1.jpg?3478",
    },
    {
        "id": 5,
        "name": "Ranny Rice Conditioner 500ml",
        "price": 200,
        "description": "Ranny conditioner is a deeply hydrating conditioner that provides the ultimate moisturization to hair...",
        "image": "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/22/3168881/1.jpg?0427",
    },
    {
        "id": 6,
        "name": "Ceriotti Super GEK 3000 Blow Dry Hair Dryer - Black.",
        "price": 200,
        "description": "The surface of the product is made by high quality Nylon plastic which are heatproof, high strength, insulative...",
        "image": "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/21/265403/1.jpg?0548",
    },
    {
        "id": 7,
        "name": "Brazilian Wool - Black",
        "price": 200,
        "description": "The Brazilian wool 100% Acrylic Hand & Machine Knitting Yarn mimics kinky hair when braided / twist...",
        "image": "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/54/362272/1.jpg?1806",
    },
    {
        "id": 8,
        "name": "Scalp Massager",
        "price": 200,
        "description": "Designed with soft, flexible silicone bristles, our scalp massager gently stimulates blood circulation...",
        "image": "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/90/0020081/1.jpg?0315",
    },
]

# Add each product to the "products" collection in Firestore
for product in products:
    db.collection("hair_products").add(product)

print("Data has been stored in Firestore.")
