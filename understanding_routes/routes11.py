

from flask import Flask
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return 'Hi '+name+'!'

@app.route('/repeat/<num>/<name>')
def say_name_multi1(num,name):
    return (name+' ')*int(num)

@app.route('/repeat/<int:num>/<name>') # To insure the second element in the URL is an integer
def say_name_multi2(num,name):
    return (name+' ')*num


if __name__=="__main__":       
    app.run(debug=True)   

