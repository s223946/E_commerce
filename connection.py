import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("credentials.json")

fb = firebase_admin.initialize_app(cred,{"databaseURL":"https://e-commerce-17673-default-rtdb.europe-west1.firebasedatabase.app/"})
db = firestore.client() 
products_ref = db.collection("Products")

def read_products():
    
    items = []

    query = products_ref.stream()

    for doc in query: items.append(doc)
    
    return items

def get_info_about_product(title):
    return products_ref.document(title).get().to_dict()

def add_item(data_set):
    products_ref.document(f'{data_set['title']}').set(data_set)