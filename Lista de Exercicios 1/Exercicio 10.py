n = int(input("Digite a quantidade de itens da lista: "))
def lista(n):
  lista = []
  for i in range(n):
    num = int(input("Digite um valor: "))
    lista.append(num)
  print(lista)

lista(n)