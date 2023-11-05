from flask import Flask, render_template, request    
from connection import read_products, get_info_about_product, add_item

app = Flask(__name__, template_folder="app/templates")
 
@app.route('/')
def index():
    return render_template('Products.jinja',items = read_products())


@app.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        data_set = {
            'title':request.form['title'],
            'description':request.form['description'],
            'price':request.form['price'],
        }
        add_item(data_set)
    return render_template('add_product.jinja')

@app.route('/Products/<title>')
def product(title):
    product_info = get_info_about_product(title)
    return render_template('product.jinja',data=product_info)

    
