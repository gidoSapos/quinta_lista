
def isEven() -> bool:
    while True:
        try:
            num = int(input('Insira um número para verificar se é par ou impar: '))
            return True if num % 2 == 0 else False
        except ValueError:
            print('Valor não inteiro númerico. Tente novamente.')


def FactorialNumber() -> int:
    while True:
        try:
            num = int(input('insira o valor desejado: '))
            for index in range (0, num + 1):

                numeral = index * num
                fatorial = numeral * numeral
            return fatorial
        except:
            print('Valor não númerico, tente novamente.')


def maxNumber() -> int:
    while True:
        try:
            lista_num,  maior_num = [], 0

            for i in range (3):
                num = int (input(f'Insira o {i+1} numero: '))
                lista_num.append(num)

                if num > maior_num:
                    maior_num = num
            
            return maior_num
        except ValueError:
            print('Insira um valor válido.')


def AvarageElement() -> str:
    while True:
        try:

            lista_num = [float(num.strip()) for num in input('(insira separado por virgula)\nDigite os números que quer saber a média: ').split(',')] 
            return f'A média dos elementos inseridos é {sum(lista_num)/len(lista_num):.0f}'
        
        except ValueError:
            print('O valor digitado não é um número, tente novamente!!!')


def sumOfNumbers() -> float:
    while True:
        try:
            soma = 0
            lista_num = [float(num.strip()) for num in input('(insira separado por virgula)\nDigite os números que quer saber a média: ').split(',')] 

            for i in lista_num:
                soma += i
            return soma
        
        except ValueError:
            print('O valor digitado não é um número, tente novamente!!!')


def MDC() -> int:
    while True:
        try:
            numero1, numero2 = int(input('Insira o primeiro número: ')), int(input('Insira o segundo número: '))
            divisores1 = [int(num) for num in range (1, numero1 + 1) if numero1 % num == 0]
            divisores2 = [int(num) for num in range (1, numero2 + 1) if numero2 % num == 0]

            mdc = [int(num) for num in divisores1 if num in divisores2]
            return max(mdc)
        
        except ValueError:
            print('O valor digitado não é um número, tente novamente!!!')

def fibonacci() -> int:
    while True:
        try:
    
            num = int(input('Por favor insira o número para a sequencia: ').strip())
            if num <= 0: raise ValueError("")
            sequencia = [0, 1]
            while len(sequencia) < num:
                sequencia.append(sequencia[-1] + sequencia[-2])
            return sequencia[:num]
        except ValueError: print('Não pode ser letras, só números')

def isPrime() -> bool:
    while True:
        try:
            divisores = []
            numero = int(input('Insira se o valor que quer descobrir se é primo ou não: '))
            for num in range (1, numero + 1):
                divisores.append(num) if numero % num == 0 else ''
            return True if len(divisores) <= 2 else False
        except ValueError:
            print('Insira um valor valido')


def inverted_list() -> list:
    while True:
        try:
            lista_num = [float(num.strip())for num in input('Insira os números desejados: ').split(',')]
            lista_num.sort()
            return lista_num
        except ValueError: print('sem strings!!!')

def transpose() -> list:
    while True:
        try:
            matriz = []
            
            for i in range(3):
                lista = input(f"Insira lista >< {i + 1} (separado por virgula\n): ").split(',')
                lista =  [int(num.strip()) for num in lista]
                if len(lista) != 3: raise ValueError('É uma matriz 3x3. ')
                matriz.append(lista)

            matrix_transposta = [[0, 0, 0],
                                 [0, 0, 0], 
                                 [0, 0, 0]]
            
            for i in range(3):
                for j in range(3):
                     matrix_transposta[j][i] = matriz[i][j]
            print("Matrix transposta:")
            for lista in matrix_transposta:
                print(" ".join(str(num) for num in lista))
            break

        except ValueError as e: print(f"ERROU!: {e}")
