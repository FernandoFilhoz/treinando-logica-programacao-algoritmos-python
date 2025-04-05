nomeSobrenome = 'Fernando Filho'
print(f'Bem-vindo à loja do {nomeSobrenome}')

totalDoPedido = 0

#Cardapio
print("\n----- Cardápio -----")
print("Sabores:")
print("CP - Cupuaçu")
print("AC - Açaí")
print("\nTamanhos e preços:")
print("P - Pequeno  | Cupuaçu: R$9,00  | Açaí: R$11,00")
print("M - Médio    | Cupuaçu: R$14,00 | Açaí: R$16,00")
print("G - Grande   | Cupuaçu: R$18,00 | Açaí: R$20,00")
print("-------------------")
    

# Escolher sabor do pedido
while True:
    sabor = input('Escolha o sabor (CP para Cupuaçu ou AC para Açaí): ')
    if sabor in ['CP', 'AC']:
        break
    else:
        print('Sabor inválido. Tente novamente.')

# Escolher tamanho do pedido
while True:
    tamanho = input('Escolha o tamanho (P, M ou G): ')
    if tamanho in ['P', 'M', 'G']:
        break
    else:
        print('Tamanho inválido. Tente novamente.')

# Calcula o preço de acordo com o tamanho e o sabor
if sabor == 'CP':
    if tamanho == 'P':
        preco = 9
    elif tamanho == 'M':
        preco = 14
    elif tamanho == 'G':
        preco = 18
elif sabor == 'AC':
    if tamanho == 'P':
        preco = 11
    elif tamanho == 'M':
        preco = 16
    elif tamanho == 'G':
        preco = 20

# Adiciona o preço ao total do pedido
totalDoPedido += preco
print(f'Você escolheu o sabor {sabor} e o tamanho {tamanho}. O valor do seu pedido é de: R${preco:.2f}')    

# Pergunta se o cliente deseja pedir mais alguma coisa
while True:
    resposta = input('Deseja pedir mais alguma coisa? (Sim/Não): '.strip().lower())
    if resposta == 'sim':
        # Reinicia as escolhas de sabor e tamanho para um novo pedido
        while True:
            sabor = input('Escolha o sabor (CP para Cupuaçu ou AC para Açaí): ')
            if sabor in ['CP', 'AC']:
                break
            else:
                print('Sabor inválido. Tente novamente.')
        
        while True:
            tamanho = input('Escolha o tamanho (P, M ou G): ')
            if tamanho in ['P', 'M', 'G']:
                break
            else:
                print('Tamanho inválido. Tente novamente.')

        # Calcula o preço novamente de acordo com o sabor e tamanho
        if sabor == 'CP':
            if tamanho == 'P':
                preco = 9
            elif tamanho == 'M':
                preco = 14
            elif tamanho == 'G':
                preco = 18
        elif sabor == 'AC':
            if tamanho == 'P':
                preco = 11
            elif tamanho == 'M':
                preco = 16
            elif tamanho == 'G':
                preco = 20

        totalDoPedido += preco
        print(f'Você escolheu o sabor {sabor} e o tamanho {tamanho}. O valor do seu pedido é de: R${preco:.2f}')
    
    elif resposta == 'não':
        print(f'O valor total do seu pedido é de: R${totalDoPedido:.2f}')
        break
    else:
        print("Resposta inválida. Por favor, responda 'Sim' ou 'Não'.")
