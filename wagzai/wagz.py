from flask import Flask, render_template, request

from wagzai.nlp import process_query

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    response = process_query(user_input)
    return {"response": response}


if __name__ == "__main__":
    app.run(debug=True)
