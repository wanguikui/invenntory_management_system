#importing
#import <filename>
#from filename import <.....>
from flask import Flask, render_template ,request,redirect,url_for

import pygal

#calling/instanciating
app = Flask(__name__)

#creating of endpoints/routes
#1. declaration of a route
#2. a function embeded to the route

@app.route('/')
def hello_world():
    return '<h1>Welcome to web Development</h1>'

#@app.route('/home')
#def home():
    #return '<h1>Welcome to my Home Page</h1>'

#@app.route('/about')
#def about():
    #return '<h1>About Us</h1>'

#@app.route('/services')
#def services():
    #return '<h1>our Services</h1>'

#@app.route('/contact')
#def contact():
    #return '<h1>Contact Us</h1>'

@app.route ('/name/<name>')
def my_name(name):
    return f'<h1>My Name is {name}</h1>'
    

@app.route('/add/<a>/<b>')
def adding(a, b):
    sum = int(a)+int(b)
    return str(sum)


@app.route('/divide/<x>/<y>')
def dividing (x, y):
    sum = int(x)/int(y)
    return str(sum)

@app.route('/multiply/<p>/<t>')
def multiplying (p, t):
    sum = int(p)*int(t)
    return str(sum)

@app.route('/bio/<name>/<age>/<town>')
def my_story(name, age, town):
    return f'My name is: {name} <p> I am {age} Years Old <p>  I live in: {town}'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_uss():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/inventories',methods= ['GET','POST'])
def inventories():
    if request.method=='POST':
        name= request.form['name']
        inv_type= request.form['type']
        buying_price= request.form['buying_price']
        selling_price= request.form['selling_price']

        print(name)
        print(inv_type)
        print(buying_price)
        print(selling_price)

        
        

        return redirect(url_for('inventories'))
        


    return render_template('inventories.html')


@app.route('/add_stock', methods=['POST'])
def add_stock():
    if request.method=='POST':
        stock = request.form['stock']
        print(stock)

        return redirect(url_for('inventories'))

@app.route('/make_sale', methods=['POST'])
def make_sale():
    if request.method=='POST':
        make_sale= request.form['quantity']
        print(make_sale)

        return redirect(url_for('inventories'))


@app.route('/edit_inv', methods=['POST'])
def edit_inv():
    if request.method=='POST':
        name= request.form['name']
        inv_type= request.form['type']
        buying_price= request.form['buying_price']
        selling_price= request.form['selling_price']

        print(name)
        print(inv_type)
        print(buying_price)
        print(selling_price)

        return redirect(url_for('inventories'))

@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')


@app.route('/data_visualization')
def data_visualization():
    pie_chart = pygal.Pie()

    pie_chart.title ='Distribution of Corona Virus in Kenya'

    pie_chart.add('Nairobi',63)
    pie_chart.add('Mombasa',20)
    pie_chart.add('Kilifi',17)
    pie_chart.add('Machakos',30)
    pie_chart.add('Kiambu',7)

    pie_data = pie_chart.render_data_uri()

    #return pie_chart.render()

    line_graph = pygal.Line()

    line_graph.title = 'Browser usage eveolution (in %)'
    line_graph.x_labels = map(str,range(2002,2013))
    line_graph.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_graph.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_graph.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_graph.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    
    #return line_graph.render()

    line_data = line_graph.render_data_uri()

    return render_template('charts.html',pie=pie_data,line=line_data)




#run your app
if __name__ == '__main__':
    app.run()
