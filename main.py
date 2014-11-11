###Convertisseur : de la base Shadok en décimal###

def sha2dec():
  a=input("Entrer un nombre en Shadok : ")
  b=a
  b=b.replace('ga','0').replace('bu','1').replace('zo','2').replace('meu','3')
  S=0
  l=len(b)-1
  for chiffre in b:
    S=S+int(chiffre)*4**1
    l=l-1
  print(S)
print(sha2dec())


