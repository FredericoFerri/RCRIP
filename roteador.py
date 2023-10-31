# Dicionário para armazenar os roteadores
roteadores = []

# Instanciação de roteadores
with open('roteadores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        partes = linha.split()
        if len(partes) == 3:
            host_name, host, port = partes
            roteador = {
                'hostName': host_name,
                'HOST': host,
                'PORT': port
            }
            roteadores.append(roteador)

#TESTE
for roteador in roteadores:
    print(f"Nome do Host: {roteador['hostName']}, HOST: {roteador['HOST']}, PORTA: {roteador['PORT']}")
