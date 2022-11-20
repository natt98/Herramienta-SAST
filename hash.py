import hashlib
from urllib import request

r = request.urlopen("https://es.wikipedia.org/wiki/MD5")
with open("md5.html", "wb") as f:
    f.write(r.read())
r.close()

texto_claro = input('Escribe el texto a cifrar: ')

h = hashlib.md5(texto_claro.encode())
firma = h.hexdigest() 

print('El texto firmado es ' + firma)

def numeros(firma):
    cant_num = len([num for num in firma if num.isdigit()])

cantidad_num = numeros(firma)
cantidad_letras = len(firma) - cantidad_num

print('La firma contiene ' + len(firma)+ ' caracteres: ' + cantidad_num + ' números y ' + cantidad_letras + ' letras.')
