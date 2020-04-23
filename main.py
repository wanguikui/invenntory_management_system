#importing
#import <filename>
#from filename import <.....>
from flask import Flask, render_template ,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

from markupsafe import Markup

from Config.Config import Development, Production


import pygal

import psycopg2




#calling/instanciating
app = Flask(__name__)


#Loading configurations
app.config.from_object(Production)

#instanciating SQLAlchemy
db=SQLAlchemy(app)

#conn = psycopg2.connect(" dbname='inventory_management_system' user='postgres' host='localhost' port='5432' password='wagatagati12!' ")

conn= psycopg2.connect("user='gilkahqjevhnwe' host='ec2-52-201-55-4.compute-1.amazonaws.com' dbname='d6sa56nv73mkjh' port='5432' password='16cf303eb194d57d2ed6514153ce474dca171a7914266a5b09c4df9d520e70ed'")
                
cur = conn.cursor()

#creating tables
from models.Inventory import InventoryModel
from models.Sales import SalesModel
from models.Stock import StockModel
    
@app.before_first_request
def create_tables():
    db.create_all()

#creating of endpoints/routes
#1. declaration of a route
#2. a function embeded to the 



#@app.route('/base.html')
#def hello_world():
    
    #return '<h1>Welcome to web Development</h1>'

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

@app.route('/')
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

    inventories=InventoryModel.fetch_all_inventories()
    
    cur.execute("""
SELECT invid, SUM(quantity)as "remaining_stock"
FROM(
SELECT st.invid, SUM(quantity)as "quantity"
	FROM public.new_stock as st
	GROUP BY invid
	
	UNION ALL
	
SELECT sa.invid, -SUM(quantity)as "quantity"
	FROM public.new_sales as sa
	GROUP BY invid
	)
	stsa
	GROUP BY invid
	ORDER BY invid;
    
    
    
    
    """)
    remaining_stock=cur.fetchall()
    print(remaining_stock)



    if request.method=='POST':
        name= request.form['name']
        inv_type= request.form['type']
        
        buying_price= request.form['buying_price']
        selling_price= request.form['selling_price']

        print(name)
        print(inv_type)
        print(buying_price)
        print(selling_price)

        new_inv= InventoryModel(name=name,inv_type=inv_type,buying_price=buying_price,selling_price=selling_price)
        new_inv.add_inventories()
        
        
        flash(Markup('Inventory added Successfully'),'success')

        return redirect(url_for('inventories'))
        


    return render_template('inventories.html', inventories=inventories,remaining_stock=remaining_stock)


@app.route('/add_stock/<invid>', methods=['POST'])
def add_stock(invid):
    #print(invid)
    if request.method=='POST':
        stock = request.form['stock']
        #print(stock)

        new_stock=StockModel(quantity=stock,invid=invid)
        new_stock.add_stock()

        return redirect(url_for('inventories'))

@app.route('/make_sale/<invid>', methods=['POST'])
def make_sale(invid):
    print(invid)


    cur.execute(f"""
    SELECT invid, sum(quantity) as "remaining_stock" 		
FROM (SELECT st.invid, sum(quantity) as "quantity" 		
FROM public.new_stock as st 		
GROUP BY invid 			 			
union all 			  			
SELECT sa.invid, - sum(quantity) as "quantity" 		
FROM public.new_sales as sa 		
GROUP BY invid) as stsa 		
WHERE invid={invid}		
GROUP BY invid; 
    
    """)

    stock=cur.fetchall()
    print(stock)



    if request.method=='POST':
        make_sale= request.form['quantity']
        print(make_sale)

        if int (stock[0][1]) > int (make_sale):

            new_sale=SalesModel(quantity=make_sale,invid=invid)
            new_sale.add_sale()
        else:
            return 'no stock'


        return redirect(url_for('inventories'))


@app.route('/edit_inv/<invid>', methods=['POST'])
def edit_inv(invid):
    record=InventoryModel.query.filter_by(id=invid).first()

    
    if request.method=='POST':
        name= request.form['name']
        inv_type= request.form['type']
        buying_price= request.form['buying_price']
        selling_price= request.form['selling_price']

        print(name)
        print(inv_type)
        print(buying_price)
        print(selling_price)

        if record:
            record.name = name
            record.inv_type = inv_type
            record.buying_price = buying_price
            record.selling_price = selling_price

            db.session.commit()

        return redirect(url_for('inventories'))

@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')


@app.route('/data_visualization')
def data_visualization():

    

    cur.execute("""
    SELECT type, count(type)
	FROM public.inventories
	GROUP BY type;
    """)

    product_service = cur.fetchall()
    print(product_service)

    pie_chart = pygal.Pie()

    #my_pie_data = [
    #('Nairobi',63),
    #'Mombasa',20),
    #('Kilifi',17),
    #('Machakos',30),
    #('Kiambu',7)
    #]
    pie_chart.title="Distibution of Fruits and Vegetables"
    for each in product_service:
    
        pie_chart.add(each[0],each[1])

        pie_data=pie_chart.render_data_uri()
     

    #pie_chart.title ='Distribution of Corona Virus in Kenya'

    #pie_chart.add()
    #pie_chart.add()
    #pie_chart.add()
    #pie_chart.add()
    #pie_chart.add()

    #pie_data = pie_chart.render_data_uri()

    #return pie_chart.render()

    line_graph = pygal.Line()

    cur.execute("""
    SELECT EXTRACT(MONTH FROM s.created_at) as sales_month, sum(quantity*selling_price)as total_sales
    from sales as s
    join inventories as i on s.invid = i.id
    GROUP BY sales_month
    ORDER BY sales_month asc
    
    """)
    monthly_sales= cur.fetchall()
    print(monthly_sales)

    #Represents sales made every month
    #data=[

        #{'month':'January', 'total':22},
        #{'month':'February', 'total':27},
        #{'month':'March', 'total':23},
        #{'month':'April', 'total':20},
        #{'month':'May', 'total':12},
        #{'month':'June', 'total':32},
        #{'month':'July', 'total':42},
        #{'month':'August', 'total':72},
        #{'month':'September', 'total':52},
        #{'month':'October', 'total':42},
        #{'month':'November', 'total':92},
        #{'month':'December', 'total':102},
    #]
    a=[]
    b=[]
    for each in monthly_sales:
        a.append(each[0])
        b.append(each[1])
        
    
    line_graph.title="Total Sales"
    line_graph.x_labels=a
    line_graph.add('total_sales',b)
    line_data=line_graph.render_data_uri()



    #line_graph.title = 'Browser usage eveolution (in %)'
    #line_graph.x_labels = map(str,range(2002,2013))
    #line_graph.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    #line_graph.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    #line_graph.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    #line_graph.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    
    #return line_graph.render()

    #line_data = line_graph.render_data_uri()

    return render_template('charts.html',pie=pie_data,line=line_data)

@app.route('/view_sales/<invid>')
def view_sales(invid):

    sales=SalesModel.get_sales_by_id(invid)
    inv_name=InventoryModel.query.filter_by(id=invid).first()
    

    return render_template('view_sales.html', sales=sales,invid=invid, inv_name=inv_name)

@app.route('/delete/<invid>')
def delete_inventory(invid):
    #print(invid)
    record=InventoryModel.query.filter_by(id=invid).first()
    if record:
        db.session.delete(record)
        db.session.commit()
    else:
        print('Record does not exist')
    
    flash('Record Deleted','danger')
    
    return redirect(url_for('inventories'))


#run your app
if __name__ == '__main__':
    app.run()
