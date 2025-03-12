lista = [3,2,6,5,7,9,1,24,32,18]

def pares(lista):
  soma = 0
  for n in lista:
    if  n % 2 == 0:
      soma += n
  return soma

print(pares(lista))