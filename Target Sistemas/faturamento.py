import json

# Suponha que o faturamento diário seja carregado de um arquivo JSON
faturamento_json = '''{
    "faturamento_diario": [0, 22174.1664, 24537.6698, 0, 26139.6134, 0, 26742.6612, 
                           0, 0, 29847.6653, 0, 0, 0, 0, 18419.2614, 0, 0, 0, 26900.7021, 
                           0, 0, 0, 0, 0, 48924.2448, 0,  0, 0, 0, 0]
}'''

dados = json.loads(faturamento_json)
faturamento = [f for f in dados['faturamento_diario'] if f > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_faturamento = sum(faturamento) / len(faturamento)
dias_acima_media = len([f for f in faturamento if f > media_faturamento])

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
