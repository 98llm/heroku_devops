import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    lista = []
    rotativo = 0
    nprimos = 0
    numero = 0
    while nprimos < 100:
        divisores_q = 0
        for i in range(1, numero+1):
            if numero % i == 0:
                divisores_q += 1
                rotativo = i
        numero += 1
        if divisores_q == 2:
            lista.append(rotativo)
            nprimos += 1
    return str(lista).strip('[]')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
