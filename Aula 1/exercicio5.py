usuarios = [
{"id": 1, "nome": "Ana", "email": "ana@email.com", "ativo": True},
{"id": 2, "nome": "Beatriz", "email": "bea@email.com", "ativo": False},
{"id": 3, "nome": "Carlos", "email": "car@email.com", "ativo": True}
]

emails_ativos = []

for usuario in usuarios:
    if usuario['ativo']:
        emails_ativos.append(usuario) #jeito comum 

for i in usuarios:
    if i['ativo']:
        emails_ativos.append(i['email']) #usar sempre o i para ficar mais simples
print("Emails ativos:")
for i in emails_ativos:
    print(i)      

