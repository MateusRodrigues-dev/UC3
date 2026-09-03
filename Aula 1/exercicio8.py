estoque = [
    {"id": 1,"nome":"Senhor dos Aneis" ,"quantidade": 10, "preco": 150.00},
    {"id": 2,"nome":"Arquitetura de software" ,"quantidade": 15, "preco": 300.00},
    {"id": 3,"nome": "Pequeno Príncipe" ,"quantidade": 2, "preco": 80.00},
]


for i in estoque:
    patrimonio += i['quantidade'] * i['preco']

print(f"O patrimônio total da empresa é de R${patrimonio:.2f}")

