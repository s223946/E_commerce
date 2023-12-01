from abc import ABC, abstractmethod

import firebase_admin
from firebase_admin import credentials, firestore

class DatabaseConnection(ABC):

    cred = credentials.Certificate("credentials.json")
    fb = firebase_admin.initialize_app(cred,{"databaseURL":"https://e-commerce-17673-default-rtdb.europe-west1.firebasedatabase.app/"})
    db = firestore.client()

    # products_ref = db.collection("Products")

    # def read_products(self):
       
    #     items = []

    #     query = self.products_ref.stream()

    #     for doc in query: items.append(doc)
        
    #     return items

    @abstractmethod
    def get_info_about_item(self,title):
        pass
        # return self.products_ref.document(title).get().to_dict()

    @abstractmethod
    def add_item(self,data_set):
        pass
        # self.products_ref.document(f'{data_set['title']}').set(data_set)

class Product(DatabaseConnection):
    
    products_ref = DatabaseConnection.db.collection("Products")

    def read_products(self):
       
        items = []

        query = self.products_ref.stream()

        for doc in query: items.append(doc)
        
        return items

    def get_info_about_item(self,title):
        return self.products_ref.document(title).get().to_dict()

    def add_item(self,data_set):
        self.products_ref.document(f'{data_set['title']}').set(data_set)

# class User(DatabaseConnection): # here might be implemented user handling