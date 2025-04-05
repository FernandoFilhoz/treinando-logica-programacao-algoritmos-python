def valida_int(pergunta, min, max):
   x = int(input(pergunta))
   while ((x < min) or (x > max)):
    x = int(input(pergunta))
   return x 

def fatorial(num):
    """
    Função que calcula a fatorial
    :param num:
    :return:
    """
    fat = 1
    if num == 0:
      return fat
#essa parte só executa caso num > 0
    for i in range (1, num + 1):
        fat *= i
    return fat

x = int(input('Digite um valor para calcular a fatorial: '))
print(f'{x}!= {fatorial(x)}')