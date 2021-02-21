from random import randint

jogador = int
continuar = 'S'
vMenor = 1
vMaior = 1

while vMenor == 1:
    valorMenor = int(input('Qual o menor valor que deseja adivinhar? '))
    if valorMenor >= 0:
        vMenor = 0
    else:
        print('Valor inválido, digite novamente')
while vMaior == 1:
    valorMaior = int(input('Qual o maior valor que deseja adivinhar? '))
    if valorMaior > 0 and valorMaior > valorMenor + 1:
        vMaior = 0
    else:
        print('Valor inválido, digite novamente')

while continuar == 'S':
    computador = int(randint(valorMenor, valorMaior))
    while jogador != computador:
        jogador = int(input('Adivinhe o valor entre 0 e 10: '))
        if jogador + 5 < computador:
            print('Você chutou muito baixo!')
        elif jogador - 5 > computador:
            print('Você chutou muito alto!')
        elif jogador == computador:
            print('ACERTOU!')
        else:
            print('Você está próximo!')
    continuar = str(input('Continuar [S/N]: ')).upper()