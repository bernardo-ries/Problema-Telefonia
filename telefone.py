import json

tabela_hash = {}

with open("telephony_sessions.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if not linha:
            continue

        try:
            telefone, dados_json = linha.split(";", 1)
            telefone = telefone.strip()
            dados_json = dados_json.strip()

            dados_dict = json.loads(dados_json)

            tabela_hash[telefone] = dados_dict
        except ValueError as e:
            print(f"Erro ao processar linha: {linha}")
            print(e)




tel = input("Digite o numero de telefone para pesquisar: ")

print ("Abaixo as informações: \n\n\n")
if tel in tabela_hash:
    print(tabela_hash[tel])
else:
    print (f"O telefone: {tel} nao esta dentro dos arquivos de telefone, tente outro.")
