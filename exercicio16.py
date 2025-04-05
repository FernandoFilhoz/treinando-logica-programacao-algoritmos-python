#Boas vindas
def boasVindas():
    nomeSobrenome = 'Fernando Filho'
    print(f'Boas-vindas à Copiadora do {nomeSobrenome}')

# Função para escolher o serviço
def escolhaServico():
    while True:
        # Opções de serviço
        print('Entre com o tipo de serviço desejado:')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')

        # Solicitando a escolha do serviço
        servico = input('Escolha o serviço desejado: ').strip().upper()
        
        # Verificando se o serviço é válido
        if servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            if servico == 'DIG':
                return 1.10  # Custo por Digitalização
            elif servico == 'ICO':
                return 1.00  # Custo por Impressão Colorida
            elif servico == 'IPB':
                return 0.40  # Custo por Impressão Preto e Branco
            elif servico == 'FOT':
                return 0.20  # Custo por Fotocópia
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente.')

# Determinar o número de páginas com desconto
def numDePaginas():
    while True:
        try:
            # Solicitar número de páginas
            numeroDePaginas = int(input('Informe o número de páginas: '))
            
            if numeroDePaginas >= 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
                continue
            
            # Aplicar o desconto conforme o número de páginas
            if numeroDePaginas >= 2000:
                numeroDePaginas_com_desc = numeroDePaginas * 0.75  # 25% de desconto
            elif numeroDePaginas >= 200:
                numeroDePaginas_com_desc = numeroDePaginas * 0.80  # 20% de desconto
            elif numeroDePaginas >= 20:
                numeroDePaginas_com_desc = numeroDePaginas * 0.85  # 15% de desconto
            else:
                numeroDePaginas_com_desc = numeroDePaginas  # Sem desconto
            
            return numeroDePaginas_com_desc
        except ValueError:
            print('Por favor, digite um número válido para as páginas.')

# Função para escolher o serviço adicional
def servicoExtra():
    while True:
        print('Deseja adicionar algum serviço:')
        print('1 - Encadernação Simples (R$ 15.00)')
        print('2 - Encadernação Capa Dura (R$ 40.00)')
        print('0 - Não desejo mais nada')
        
        try:
            adicional = int(input('Escolha o serviço extra: '))
            if adicional == 1:
                return 15.00  # Encadernação Simples
            elif adicional == 2:
                return 40.00  # Encadernação Capa Dura
            elif adicional == 0:
                return 0.00  # Nenhum Adicional
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Opção inválida. Tente novamente.')

# Função principal
def main():
    # Exibindo boas-vindas
    boasVindas()
    # Escolhendo o serviço
    servico = escolhaServico()
    # Escolhendo o número de páginas
    numeroDePaginas_com_desc = numDePaginas()
    # Escolhendo o serviço extra
    extra = servicoExtra()
    # Calculando o valor total
    total = (servico * numeroDePaginas_com_desc) + extra
    
    # Exibindo o valor total
    print(f'Total: R${total:.2f} (servico: {servico} * páginas: {numeroDePaginas_com_desc} + extra: {extra})')

# Chamando a função principal
if __name__ == "__main__":
    main()
