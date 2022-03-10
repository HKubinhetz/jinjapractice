# Creating a Web Application by using Flask and Jinja!
import datetime
import getinfo
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    currentyear = str(datetime.datetime.now()).split("-")[0]
    return render_template("index.html", year=currentyear)


@app.route("/guess/<username>")
def name_analysis(username):
    age = getinfo.get_age(username)
    gender = getinfo.get_gender(username)
    return render_template("guess.html",
                           name=username.capitalize(),
                           age=age,
                           gender=gender)


if __name__ == "__main__":
    app.run(debug=True)


