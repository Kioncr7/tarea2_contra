import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
extencion = int(input("Escribe de cuantos caracteres quieres que sea la contraseña:"))
contrasena = ""

for i in range(extencion):
    contrasena += random.choice(caracteres)
print(contrasena)
