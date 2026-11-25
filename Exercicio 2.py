print ("Bem-vindo Ana!")
while True: 
    try:
        cafe = int(input (" Quanto que você gastou no café hoje? "))
        print ("Você gastou R$ " + str (cafe) + " no café, anotado :)")
        break
    except ValueError:
        print ("Ops, houve um pequeno erro. Tente digitar só algarismos, por exemplo, 8")
while True: 
    try:
        almoco = int (input ("Quanto que você gastou no almoço hoje? "))
        print ("Você gastou R$ " + str (almoco) + " no almoço, anotado :)")
        break
    except ValueError:
        print ("Ops, houve um pequeno erro. Tente digitar só algarismos, por exemplo, 8")
while True: 
    try:
        transporte = int (input ("Quanto que você gastou no transporte hoje? "))
        print ("Você gastou R$ " + str (transporte) + " no transporte, anotado :)")
        break
    except ValueError:
        print ("Ops, houve um pequeno erro. Tente digitar só algarismos, por exemplo, 8")
total = (cafe + almoco + transporte)
print ("Hoje você gastou um total de R$ " + str (total))