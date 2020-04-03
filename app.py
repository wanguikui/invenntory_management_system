#importing
#import <filename>
#from filename import <.....>
from flask import Flask

#calling/instanciating
app = Flask(__name__)

#creating of endpoints/routes
#1. declaration of a route
#2. a function embeded to the route

@app.route('/')
def hello_world():
    return '<h1>Welcome to web Development</h1>'

@app.route('/home')
def home():
    return '<h1>Welcome to my Home Page</h1>'

@app.route('/about')
def about():
    return '<h1>About Us</h1>'

@app.route('/services')
def services():
    return '<h1>our Services</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact Us</h1>'

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

#run your app
if __name__ == '__main__':
    app.run()
