from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = ""

    if request.method == "POST":
        long_url = request.form["long_url"]

        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)

    return render_template("index.html", short_url=short_url)

if __name__ == "__main__":
    app.run(debug=True)
