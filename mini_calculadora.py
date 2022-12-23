print("Programa\n")
try:
    a1 = int(input("introduce un primer número: "))
    a2 = int(input("introduce un segundo número: "))
    a3 = 0

    eleccion = int(input("que quieres hacer?\n1.-suma\n2.-resta\n"))

    if eleccion == 1:
        a3 = a1 + a2
        print(f"la suma es {a3}")
    elif eleccion == 2:
        a3 = a1 - a2
        print(f"la resta es {a3}")
    else:
        print(f"no existe")
except:
    print("no se pudo")