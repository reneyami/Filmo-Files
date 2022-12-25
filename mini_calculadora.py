print("Programa")
def calculadora():
    try:
        a1 = int(input("introduce un primer número: "))
        a2 = int(input("introduce un segundo número: "))

        eleccion = int(input("que quieres hacer?\n1.-suma\n2.-resta\n3.-division\n"))

        if eleccion == 1:
            a3 = a1 + a2
            print(f"la suma es {a3}")
        elif eleccion == 2:
            a3 = a1 - a2
            print(f"la resta es {a3}")
        elif eleccion == 3:
            a3 = a1 / a2
            print(f"la division es: {a3}")
        else:
            print(f"no existe")
    except ZeroDivisionError:
            result = 0
            print(f"el resultado es: {result}")
    except:
        print(f"no debes usar letras, sino números")

calculadora()