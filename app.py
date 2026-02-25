from flask import Flask, request, jsonify
from flask_cors import CORS

from services.conversor import binario_para_decimal_e_hex
from utils.validacoes import binario_valido

app = Flask(__name__)
CORS(app)


@app.route("/api/converter", methods=["POST"])
def converter():
    data = request.get_json(silent=True) or {}
    binario = data.get("bin", "")

    if not binario_valido(binario):
        return jsonify({"error": "Binário inválido"}), 400

    decimal, hexadecimal = binario_para_decimal_e_hex(binario)

    return jsonify({
        "decimal": decimal,
        "hexadecimal": hexadecimal
    })


if __name__ == "__main__":
    app.run(debug=True)