

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route("/")
def count():
    if 'counter' in session:
        print('key exists!')
        session['counter']+=1
    else:
        print("key 'key_name' does NOT exist")
        session['counter']=1
    return render_template('counter.html')

@app.route("/increament")
def count2():
    if 'counter' in session:
        print('key exists!')
        session['counter']+=1
    else:
        print("key 'key_name' does NOT exist")
        session['counter']=1
    return redirect("/")

@app.route("/increament2" , methods=['POST'])
def count3():
    x = int(request.form['num'])
    if 'counter' in session:
        print('key exists!')
        session['counter']+= (x-1)
    else:
        print("key 'key_name' does NOT exist")
        session['counter']=1
    return redirect("/")

@app.route("/destroy_session")
def remove_count():
    session.pop('counter')
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


