import random

nume_ran = random.randint(1, 100)
playing = True


while playing:
    guess = int(input("ingresa un numero:"))
    if guess == nume_ran:
        playing = False
        print("felizidades eres el ganador")
        break
    elif guess > nume_ran:
        print(f"el numero que ingresaste {guess} es mayor")
    elif guess < nume_ran:
        print(f"el numero que ingresaste {guess} es menor")


    #IA del rival
    computador = random.randint(1, 100)
    if computador == nume_ran:
        playing = False
        print(f"el numero de tu rival: {computador} es el correcto")
        break
    elif computador > nume_ran:
        print(f"el numero de tu rival: {computador} es mayor")
    elif computador < nume_ran:
        print(f"el numero de tu rival: {computador} es menor")