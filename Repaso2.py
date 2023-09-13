jugador_secreto = "Owen Farrell"
intento= ""
while True:

    intro = print("Intenta adivinar el nombre del jugador de rugby: ") 
    print("Pista: Juega en la posición de apertura o centro, y es jugador actual. Tiene una caracteristica a la hora de patear que se llama el Escaner.")
    intento= input("") 
    
    jugador_secreto=jugador_secreto.upper()
    intento=intento.upper()
    if intento == jugador_secreto:
        print("¡Correcto! El jugador de rugby es: " + jugador_secreto)
        print("Saliendo del programa...")
        break
    elif intento == "SALIR":
        print("Saliendo del programa...")
        break
    elif intento =="AYUDA":
        print("Pista: Juega en la seleccion de Inglaterra con la dorsal 12")
        respuesta= input("")
        if respuesta.upper()== "OWEN FARRELL":
            print("Correcto!")
            break
        else:
            print("Incorrecto")
    else:
        print("¡Incorrecto! Intenta de nuevo o escribe 'Salir' para salir del programa.")
        print("Si desea una pista ingrese Ayuda")