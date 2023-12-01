from flask import Flask, render_template, request    
from connection import Product

app = Flask(__name__, template_folder="app/templates")
db = Product()

@app.route('/')
def index():
    return render_template('Products.jinja',items = db.read_products())

@app.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        data_set = {
            'title':request.form['title'],
            'description':request.form['description'],
            'price':request.form['price'],
        }
        db.add_item(data_set)
    return render_template('add_product.jinja')

@app.route('/Products/<title>')
def product(title):
    product_info = db.get_info_about_item(title)
    return render_template('product.jinja',data=product_info)

    
