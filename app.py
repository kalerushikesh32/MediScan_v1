from flask import Flask,url_for,render_template,request,redirect
import os
from engine import detector_1

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
@app.route('/home', methods = ["GET", "POST"])
def home():
    return render_template("pneumonia.html")

app.config["img_uploads"] = "C:\\Users\\lenovo\\SPE\\MediScan_v2\\static\\uploads"

@app.route('/result',methods = ["GET","POST"])
def result():
    if request.method == "POST":
        print(request.files)
        if request.files:
            image = request.files["inpFile"]
            image.save(os.path.join(app.config["img_uploads"],image.filename))
            # print("image saved")
            # print(image)
            # print(image.filename)
            predicted = detector_1(image.filename)
            return render_template("result.html",disease = predicted)
        else:
            return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)