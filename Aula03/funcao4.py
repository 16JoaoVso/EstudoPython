# Criar uma função que escreve a tabuada para um
# determinado valor definido pelo usuário em
# um arquivo de texto

def tabuada(valor):
  """Escreve a tabuada de um determinado número em um arquivo .txt"""
 
  with open("tabuada.txt", "w") as arquivo:
    for i in range(1, 11):
      arquivo.write(f"{valor} * {i} = {valor * i}\n")
 
 
if __name__ == "__main__":
  valor = int(input("Digite um número: "))
  tabuada(valor)