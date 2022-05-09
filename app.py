from flask import Flask,url_for,render_template,request,redirect
import os
from engine import detector_1
from pathlib import Path
import logging

logging.basicConfig(filename='app.log',filemode='a',
                    format='[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

app = Flask(__name__)

path_1  = os.getcwd()

print(path_1)


@app.route("/", methods = ["GET", "POST"])
@app.route('/home', methods = ["GET", "POST"])
def home():
    return render_template("pneumonia.html")

# app.config["img_uploads"] = path_1+"\\static\\uploads"            ##For Windows
app.config["img_uploads"] = path_1+"/static/uploads"                ##For Ubuntu

@app.route('/result',methods = ["GET","POST"])
def result():
    if request.method == "POST":
        print(request.files)
        if request.files:
            image = request.files["inpFile"]
            logging.info(image.filename)
            image.save(os.path.join(app.config["img_uploads"],image.filename))
            # print("image saved")
            # print(image)
            # print(image.filename)
            predicted = detector_1(image.filename)
            logging.info(predicted)
            return render_template("result.html",disease = predicted)
        else:
            return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.0', port=80)
