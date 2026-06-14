from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/google129e54bb3c59bcc2.html")
def google_verify():
    return send_from_directory(".", "google129e54bb3c59bcc2.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)