
# Using only one template

from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/play')          
def square():
    color= '#9fc5f8'
    x= 3
    return render_template('level-3.html',x=int(x),col=color)

@app.route('/play/<x>')          
def square_multi(x):
    color= '#9fc5f8'
    return render_template('level-3.html',x=int(x),col=color)

@app.route('/play/<x>/<color>')          
def square_multi_color(x,color):
    return render_template('level-3.html',x=int(x),col=color)


if __name__=="__main__":       
    app.run(debug=True)   

# ****************************************************************
# Using Different templates

# @app.route('/play')          
# def square():
#     return render_template('level-1.html')

# @app.route('/play/<x>')          
# def square_multi(x):
#     return render_template('level-2.html',x=int(x))

# @app.route('/play/<x>/<color>')          
# def square_multi_color(x,color):
#     return render_template('level-3.html',x=int(x),col=color)
