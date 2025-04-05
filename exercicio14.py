nomeSobrenome = 'Fernando Filho'

print(f'Bem vindo a Loja do {nomeSobrenome}')

valorProduto = float(input('Entre com o valor do produto: '))
quantidadeProduto = int(input('Entre com a quantidade do produto: '))

valorSemDesconto = valorProduto * quantidadeProduto

#Desconto inicializado
desconto = 0

#Verificando o desconto que ira aplicar sobre o produto
if valorSemDesconto < 2500:
    desconto = 0
elif 2500 <= valorSemDesconto < 6000:
    desconto = 4
elif 6000 <= valorSemDesconto < 10000:
    desconto = 7        
else:
    desconto = 11    


#Calculando o desconto para aplicar sob o produto
valorComDesconto = valorSemDesconto * (desconto / 100)
totalDescontado = valorSemDesconto - valorComDesconto

print(f'O valor SEM desconto: R${valorSemDesconto}')
print(f'O valor COM desconto: R${totalDescontado}')