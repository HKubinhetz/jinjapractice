# Creating a Web Application by using Flask and Jinja!
import datetime
import getinfo
import requests
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


@app.route("/blog")
def blog_post():
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)


