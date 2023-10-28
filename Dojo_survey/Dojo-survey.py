
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("survey.html")

@app.route('/users', methods=['POST'])
def take_survey():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    city= request.form['city']
    lang = request.form['lang']
    comment= request.form['comment']
    return render_template("result.html", name=name, city=city, lang=lang, comment=comment)


if __name__ == "__main__":
    app.run(debug=True)

