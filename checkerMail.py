import re

def verificadorCorreo():
    patron_De_correos = re.compile("[A-Za-z0-9]+@[a-zA-Z]+\.(com|net)$")
    while True:
        print("1 para verificar, 2 para salir")
        opcion = input()
        if opcion == "1":
            print("ingrese correo: ")
            entrada = input()
            if(re.search(patron_De_correos, entrada)):
                print("Correo Valido")
            else:
                print("Correo Invalido")
        else:
            break 

if __name__ == "__main__":
    verificadorCorreo()
