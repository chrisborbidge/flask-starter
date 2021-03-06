from flask import Flask, render_template

app = Flask(__name__)


@app.route("/health")
def health():
    return "Healthy!"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()
