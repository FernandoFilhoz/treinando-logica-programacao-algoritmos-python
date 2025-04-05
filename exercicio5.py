print('Calculadora')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer outra tecla para sair')

op = input('Qual operação você deseja realizar ?')
x = int(input('Digite o primeiro valor'))
y = int(input('Digite o segundo valor'))

if(op == '+'):
    res = x + y
    print(f'Resultado: {x} + {y} = {res}')
elif(op == '-'):
    res = x - y
    print(f'Resultado: {x} - {y} = {res}')
elif(op == '*'):
    res = x * y
    print(f'Resultado: {x} * {y} = {res}')
elif(op == '/'):
    res = x / y
    print(f'Resultado: {x} / {y} = {res}')
else:
    print('Encerrando o programa...')


