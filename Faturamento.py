import json
import Funcoes as funcoes

with open("dados.json", encoding= "utf-8") as dados_json:
    json_faturamento = json.load(dados_json)

dias = []
valores = []

for i in json_faturamento:
    valores.append(i['valor'])
    dias.append(i['dia'])


print(funcoes.buscarMenor(valores))
print(funcoes.buscarMaior(valores))
funcoes.buscarMaiorMedia(valores)