from flask import Flask, render_template, request
from prediction import preprocess, vectorizor, get_prediction

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        msg = request.form['msg']
        preprocess_text = preprocess(msg)
        vectorized_text = vectorizor(preprocess_text)
        prediction = get_prediction(vectorized_text)  # should return "Spam" or "Not Spam"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
