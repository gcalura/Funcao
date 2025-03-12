lista = [-1, 2,-35,9,-100,32,-45]

def pos(lista):

  i = 0
  for n in lista:
    if n > 0:
      i += 1
  return i

print(pos(lista))
