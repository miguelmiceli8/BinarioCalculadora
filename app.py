from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def binario_para_hex(numero):
    tamanho = len(numero)

    while tamanho % 4 != 0:
        numero = '0' + numero
        tamanho += 1

    tabela = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }

    hexadecimal = ""
    for i in range(0, tamanho, 4):
        hexadecimal += tabela[numero[i:i+4]]

    decimal = int(numero, 2)
    return decimal, hexadecimal


@app.route("/api/converter", methods=["POST"])
def converter():
    data = request.get_json()
    binario = data.get("bin")

    if not binario or not all(c in "01" for c in binario):
        return jsonify({"error": "Binário inválido"}), 400

    decimal, hexadecimal = binario_para_hex(binario)

    return jsonify({
        "decimal": decimal,
        "hexadecimal": hexadecimal
    })


if __name__ == "__main__":
    app.run(debug=True)
