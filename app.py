from flask import Flask,url_for,render_template
import os

app = Flask(__name__)


@app.route("/")
@app.route('/home', methods = ["GET", "POST"])
def home():
    return render_template("pneumonia.html")


if __name__ == "__main__":
    app.run(debug=True)