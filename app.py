from flask import Flask, request, jsonify, render_template
import minibot  # tu minibot.py

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # tu HTML

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json
    user_msg = data.get("mensaje", "")
    respuesta = minibot.responder(user_msg)  # función que debes tener en minibot.py
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
