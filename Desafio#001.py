"""
Desafio #01 - Números Primos
Jonas estava na sua aula de matemática e o conteúdo do dia era números primos, 
ele então decidiu escrever um algoritmo para calcular números primos. Para começar, 
ele gostaria de saber de todos os números de 1 até 10000 quais eram primos. Sua tarefa 
é escrever um programa que liste todos os números primos de 1 até 10000.
"""
# Por Kaigo.


# Todos os números primos obtidos
primos = []

# Pega todos os números entre 1 e 10000 (para determinar se é primo ou não)
for number in range (1, 10000):
    div = False # Necessário para resetar o estado
    # Pega todos os números até o número atual (para testar divisão)
    for inter in range(2, number-1): # Se houver alguma divisão aqui, o número não é primo, inter = intermediario
        if number % inter == 0: # Se o resto da divisão do número for 0
            div = True
            break
    if div == True: # Caso tenha ocorrido uma divisão, ele continua o programa
        continue
    primos.append(str(number)) # Não ocorreu, o número é adicionado à lista.


print('Os números primos de 1 até 10000 são:')
print(', '.join(primos)) # Formata a saída
