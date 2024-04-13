import random
while True:
    dict_fic = ["Interlestelar", 2012, "O foguete"]
    dict_açao =["Velozes e Furisos", "O vidente", 1996]
    dict_romanc = ["A culpa é das estrelas", "O virgem de 40 anos", "Sou todo seu"]

    print("1. Ficção")
    print("2. Ação")
    print("3. Romance")

    choice = input("Escolha um genêro: ")
    aleatorio = random.choice(dict_fic)
    aleatorio02 = random.choice(dict_açao)
    aleatorio03 =  random.choice(dict_romanc)


    if choice == '1':
        print(f"Que maravilha!! Seu filme é : {aleatorio}")
        break
    elif choice == '2':
        print(f"Parabéns!! Tirou a sorte grande. Aqui vai um belo filme para você: {aleatorio02}")
        break
    elif choice == '3':
        print(f"Oba! Sua sugestão de filme é: {aleatorio03}")
        break
