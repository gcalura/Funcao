texto = input("Digite uma palavra: ")
def inv(texto):
  if texto[:: - 1] == texto:
    return True
  else:
    return False
inv(texto)
