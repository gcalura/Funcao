n = int(input("Digite um valor: "))

def pI(n):
  if n % 2 == 0:
    return "Par"
  else:
    return "Impar"
  print(pI(n))
pI(n)
