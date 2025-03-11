plv = input("Digite uma Palavra: ").upper()
vog = ("A,E,I,O,U")

def vogais(plv):
  contador = 0
  for i in plv:
    if i in vog:
      contador += 1
  return contador

print(vogais(plv))