cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    terminar = input('Deseja cadastar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = input('Qual o ano de nascimento?')
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['ano'].append(ano)

print(cadastro)    