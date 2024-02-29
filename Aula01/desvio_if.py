# Pede um número e verifica se é par ou impar
numero = input("Digete um número: ")
# È necessário realizar na conversão de texto para número, pois a função input sempre retorna o valor em forma de texto.
# Então utilizamos a função int para converter a variável numero em valor numérico inteiro e assim realizar o cálculo.
numero = int(numero)


if(numero % 2 == 0):
    print("O número digitado é Par")
else:
    print("O número digitado é impar")