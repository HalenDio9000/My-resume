from flask import Flask, render_template

# create our web application
app = Flask (__name__)

#Create our routes 
@app.route('/')
def home():
    return render_template('index.html')

#start our application 

    