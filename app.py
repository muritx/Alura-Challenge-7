# from fastapi import FastAPI

# app = FastAPI()

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Carregar dados dos depoimentos a partir do arquivo JSON com codificação UTF-8
with open('db.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    depoimentos = data['depoimentos']

@app.route('/')
def home():
    return 'API para alimentação do Challenge 7 - Alura'

@app.route('/depoimentos',methods=['GET'])
def obterDepoimentos():
    return jsonify(depoimentos)

@app.route('/depoimentos/<int:id>',methods=['GET'])
def obterDepoimentoPorId(id):
    for depoimento in depoimentos:
        if depoimento.get('id') == id:
            return jsonify(depoimento)

@app.route('/depoimentos/<int:id>',methods=['PUT'])
def editarDepoimentoPorId(id):
    depoimentoAlterado = request.get_json()
    for indice,depoimento in enumerate(depoimentos):
        if depoimento.get('id') == id:
            depoimentos[indice].update(depoimentoAlterado)
            return jsonify(depoimentos[indice])

@app.route('/depoimentos',methods=['POST'])
def incluirNovoDepoimento():
    novoDepoimento = request.get_json()
    depoimentos.append(novoDepoimento)
    return jsonify(depoimentos)

@app.route('/depoimentos/<int:id>',methods=['DELETE'])
def excluirDepoimento(id):
    for indice, depoimento in enumerate(depoimentos):
        if depoimento.get('id') == id:
            del depoimentos[indice]
    
    return jsonify(depoimentos)