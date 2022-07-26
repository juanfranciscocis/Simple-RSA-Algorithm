
#ELEGIR 2 NUMEROS PRIMOS CUALQUIERA

p = 11
q = 17

#OBTENER UN NUMERO QUE SEA EL PRODUCTO DE LOS DOS, ESTE NUMERO SI PUEDE SER PUBLICADO
n = p*q #187

#FUNCION PHY
phy = (p-1)*(q-1) #160

#ELEGIR UN NUMERO E, ESTE NUMERO DEBE ESTAR ENTRE  1<E<PHY ADEMAS DEBE SER COPRIMO CON "N" Y PHY
e=7

#ELEGIR UN NUMERO D, ESTE NUMERO = (D*E MOD PHY = 1)
d=23

#LLAVE PUBLICA Y PRIVADA
#PUBLICA
pubKey = [n,e]
#PRIVADA
privKey = [n,d]

#LLAVES
print("LLAVE PUBLICA: " + str(pubKey))
print("LLAVE PRIVADA: " + str(privKey))

#MENSAJE A CIFRAR
mensaje = str(input("INGRESE UN MENSAJE A CIFRAR: "))

def cifrarmensaje(mensajeCifrado, llavePublica):
    #CAMBIO DE MINUSCULAS A MAYUSCULAS
    mensajeCifrado = mensajeCifrado.upper()
    #SEPARACION POR PALABRA Y GUARDADO EN LISTA
    mensajeSeparado = mensajeCifrado.split(" ")
    #STRING FINAL DEL CIFRADO DEL MENSAJE
    cifradoMensajeCompleto = ""
    #ALMACENAMIENTO DE PALABRA EN UNA LISTA
    almacenamientoPalabra = []

    #PARA CADA PALABRA EN LA LISTA SE APLICA EL CIFRADO
    for i in mensajeSeparado:
        palabra = cifrarpalabra(i, llavePublica) #CIFRADO DE LA PALABRA EXTRAIDA
        almacenamientoPalabra.append(palabra) #ALACENAMIENTO EN LA LISTA

    #CAMBIO DE LISTA A STRING PARA MEJOR IMPRESION
    for j in almacenamientoPalabra:
        cifradoMensajeCompleto = cifradoMensajeCompleto + str(j) + " "
    return cifradoMensajeCompleto

#FUNCION QUE CAMBIA DE LETRA A NUMERO
def buscarNum(x):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    letra = 0
    for i in alfabeto:
        if x == i:
            return letra
        else:
            letra = letra + 1

def cifrarpalabra(mensaje, llavePublica):
    #GUARDADO EN LISTA DE LA PALABRA YA CIFRADA
    guardadoPalabraCifrada = []
    #GUARDADO DE LA LETRA CAMBIADA A NUMERO
    guardadoCambioLetraNum = []
    #VALORES PARA N Y E DE LA FORMULA
    n, e = llavePublica
    #STRING DE GUARDADO FINAL POR PALABRA
    cifradoPalabraCompelta = ""
#SE HACE EL CAMBIO DE LETRA A NUMERO
    for i in mensaje:
        x = buscarNum(i)
        guardadoCambioLetraNum.append(x)
#SE APLICA EL CIFRADO Y SE GUARDA LA PALABRA EN UNA LISTA
    for j in guardadoCambioLetraNum:
        c = (j ** e) % n
        guardadoPalabraCifrada.append(c)
#SEPARACION DE LA PALABRA DE LISTA A STRING
    for k in guardadoPalabraCifrada:
        cifradoPalabraCompelta = cifradoPalabraCompelta + str(k) + " "
    return cifradoPalabraCompelta

#ALAMECNAMIENTO DEL MENSAJE CIFRADO
mensajeCifrado = cifrarmensaje(mensaje,pubKey)

#IMPRESION DEL MENSAJE CIFRADO
print("MENSAJE CIFRADO: ")
print(mensajeCifrado)

#MENSAJE A DECIFRAR
mensajeDecifrado = str(input("INGRESE UN MENSAJE A DECIFRAR: "))

def descifrarmensaje(mensajeADecifrar, llavePrivada):
    #CONVERSION MINUSCULAS A MAYUSCULAS
    mensajeADecifrar = mensajeADecifrar.upper()
    #SEPARACION DE LOS NUMEROS Y GUARDADO EN LISTA
    sepNumerosYGuardado = mensajeADecifrar.split("  ")
    # STRING FINAL DEL DECIFRADO DEL MENSAJE
    decifradoDeMensajeCompleto = ""
    #GUARDADO DEL MENSAJE YA DECIFRADO PERO EN LISTA
    mensajeDecifradoGuardado = []

    #DECIFRAR PALABRA POR PALABRA Y GUARDADO DE LA MISMA EN UNA LISTA
    for i in sepNumerosYGuardado:
        palabra = descifrarnumero(i, llavePrivada)
        mensajeDecifradoGuardado.append(palabra)
    #MEJORA DE IMPRESION, PASO DE LISTA A STRING
    for j in mensajeDecifradoGuardado:
        decifradoDeMensajeCompleto = decifradoDeMensajeCompleto + str(j) + " "
    return decifradoDeMensajeCompleto


def descifrarnumero(mensajeNumerico, llave):
    #GUARDADO DEL DECIFRADO EN NUMEROS
    decifradoNumericoGuardado = []
    #SEPARACION DEL STRING EN NUMEROS
    separacionPorNumerosGuardado = []
    #VALORES PARA N Y E DE LA FORMULA
    n, d = llave
    #ENCADENAMIENTO FINAL PARA IMPRESION
    encadenamientoEnString = ""
    #STRING SEPARADO
    mensajeNumericoGuardado = mensajeNumerico.split(" ")

    #SEPARACION DEL STRING Y GUARDADO POR NUMERO EN UNA LISTA
    for i in mensajeNumericoGuardado:
        x = int(i)
        separacionPorNumerosGuardado.append(x)

    #SE APLICA LA FORMULA PARA DESENCRIPTAR EL MENSAJE, SIGUE SIENDO EN VALORES NUMERICOS PERO YA ESTA DESENCRIPTADO
    for j in separacionPorNumerosGuardado:
        m = (j ** d) % n
        decifradoNumericoGuardado.append(m)

    #CAMBIO DE NUMEROS A LETRAS LEGIBLES
    for k in decifradoNumericoGuardado:
        cambioNumeroLetra = buscarlet(k)
        encadenamientoEnString = encadenamientoEnString + str(cambioNumeroLetra)
    return encadenamientoEnString


#CAMBIO DE NUMERO A LETRA
def buscarlet(x):
    alf = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    c = 0
    for i in alf:
        if x == c:
            return i
        else:
            c = c + 1


#ALMACENAMIENTO DEL MENSAJE DECIFRADO
mensajeDecifrado = descifrarmensaje(mensajeDecifrado, privKey)

#IMPRESION DEL MENSAJE DECIFRADO
print("MENSAJE DECIFRADO: ")
print(mensajeDecifrado)




