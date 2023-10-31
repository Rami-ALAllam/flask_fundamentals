

from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/play')          
def checkboard():
    return render_template('check.html')

@app.route('/play/<x>')          
def checkboard2(x):
    y=int(x)
    return render_template('check2.html',x=int(y))

@app.route('/play/<x>/<y>')          
def checkboard3(x,y):
    x1=int(x)
    y1=int(y)
    return render_template('check3.html',x=x1, y=y1)

@app.route('/play/<x>/<y>/<col1>/<col2>')          
def checkboard4(x,y,col1,col2):
    x1=int(x)
    y1=int(y)
    colxx=col1
    colyy=col2
    return render_template('check4.html',x=x1, y=y1, colx=colxx, coly=colyy)

if __name__=="__main__":       
    app.run(debug=True)   

