from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("page1.html", name=name)
    return render_template("index.html")

@app.route("/funny/<name>")
def funny(name):
    return render_template("page2.html", name=name)

@app.route("/motivation/<name>")
def motivation(name):
    return render_template("page3.html", name=name)

@app.route("/blessings/<name>")
def blessings(name):
    return render_template("page4.html", name=name)

if __name__ == "__main__":
   app.run(host="0.0.0.0",port = 10000)