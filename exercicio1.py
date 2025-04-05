preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto do produto 0-100%: '))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f'O preço do produto é {preco}. E tem desconto de {percentual}')
print(f'Valor calculado de desconto: {desconto}. Valor final do produto 500 {final}')