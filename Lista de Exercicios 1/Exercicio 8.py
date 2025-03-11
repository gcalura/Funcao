n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
n4 = int(input("Digite um valor: "))
n5 = int(input("Digite um valor: "))
n6 = int(input("Digite um valor: "))
n7 = int(input("Digite um valor: "))
notas = [n1,n2,n3,n4,n5,n6,n7]
soma = sum(notas)
def media(notas):
  return soma / 7
  print(media(notas))
media(notas)