lista = [3,2,6,5,7,9,1,24,32,18]
def m3(lista):
  i  = 0
  for n in lista:
    if n % 3 == 0:
      i += 1
  return i
print(m3(lista))