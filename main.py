def space():
    print("--------------------------------------------------------------------------------")

def Project2():
    CMD_BED = 'b'
    CMD_CLOSE = 'c'
    CMD_EAST = 'e'
    CMD_FEED = 'f'
    CMD_GET = 'g'
    CMD_LOCK = 'l'
    CMD_NORTH = 'n'
    CMD_OPEN = 'o'
    CMD_PUT = 'p'
    CMD_QUIT = 'q'
    CMD_SOUTH = 's'
    CMD_TV = 't'
    CMD_UNLOCK = 'u'
    CMD_WEST = 'w'

    ROOM_FRONT = 0
    ROOM_LIVING = 1
    ROOM_KITCHEN = 2
    ROOM_OFFICE = 3
    ROOM_BED = 4

    ROOM_NAMES = ("Bathroom", "Hallway", "Vault", "Denon Alley", "Place du Carrousel")

    flag_me_awake = True
    flag_tv_on = False
    safe = False
    key = False
    locked = True
    op = False
    bone = False
    stella = False
    spam = False
    spamr = True

    room = 0
    turn = 0

    space()

    print(
        ">> A murder in Paris' Louvre Museum and cryptic clues in some of Leonardo da Vinci's")
    print("most famous paintings lead to the discovery of a religious mystery.")
    print("For 2,000 years a secret society closely guards information that")
    print("-should it come to light- could rock the very foundations of Christianity.")
    print()
    print("CIIC 3015 Autumn 2021 Project 2: The Da Vinci Code")
    print()
    space()
    while flag_me_awake:
        print("Location: ", ROOM_NAMES[room])
        cmd = input("> ")
        turn += 1
        space()

        if cmd == CMD_QUIT:
            return False

        if room == ROOM_FRONT:
            if cmd == CMD_EAST:
                print("\N{bomb}" + " We have little time before the police comes back, hurry up!! " + "\N{bomb}")
                space()
                print(">> You threw the GPS through the window to fool the Police, they will ")
                print("get a couple of minutes until they find out the trick")
                space()
                print("You enter the Museum Hallway")
                if flag_tv_on == False:
                    print("The Lights are ON")
                if stella == False:
                    print("Shhhh, there's a police officer around here")
                if stella == True:
                    print("The officer is knocked out... hope he is just knocked out... ")
                room = ROOM_LIVING
                continue

        if room == ROOM_LIVING:
            if cmd == CMD_TV:
                if flag_tv_on:
                    print("You turn ON the lights.")
                else:
                    print("You turn OFF the lights.")
                flag_tv_on = not flag_tv_on
                continue

            if cmd == CMD_WEST:
                print("We don't have to go in there again")
                continue

        if room == ROOM_LIVING:
            if cmd == CMD_EAST:
                print("You enter the Denon Alley")
                if safe == True:
                    print("The Cryptex is open")
                if safe == False:
                    print("There's a Cryptex behind the Mona Lisa, we should open it")
                room = ROOM_OFFICE
                continue

        if room == ROOM_OFFICE:
            if cmd == CMD_OPEN:
                print("Be careful, if you put the wrong password,")
                print(("the content of the Cryptex will break"))
                print("-Resolve this 3 puzzles-")
                print("<< Including the 0, it's the 9th position")
                print(("in the Fibonacci sequence >>"))
                pas = int(input("Number: "))
                print("<< __ Oiram Repus was a game very ")
                print("popular in Odnetnin >>")
                pas2 = int(input("Number: "))
                print("<< It was known as the Year of the Consulship")
                print("of Athenobarbus and Camilus >>")
                pas3 = int(input("Password? "))
                if pas == 21:
                    if pas2== 64:
                        if pas3 == 32:
                            print('Open ')
                            print('What? A Fleur-de-Lys Key... RIGHT! This might open the Vault')
                            safe = True
                            continue
                else:
                    print("The inside has been destroyed ")
                    space()
                    print("YOU LOST")
                    break

        if room == ROOM_OFFICE:
            if cmd == CMD_GET:
                if safe == True:
                    print("Got the key ")
                    key = True
                    continue
                elif safe == False:
                    print("Cryptex is not open")
                    continue

        if room == ROOM_OFFICE:
            if cmd == CMD_PUT:
                if key == True and safe == True:
                    print("You put the key in the Cryptex")
                    key = False
                elif key == False:
                    print("You don't have any key")
                elif key == True and safe == False:
                    print("The Cryptex is locked, but be careful, you just have ONE try")
                continue

        if room == ROOM_OFFICE:
            if cmd == CMD_CLOSE:
                if safe == False:
                    print("Its already closed")
                if safe == True:
                    print("Cryptex closed")
                    safe = False
                continue

        if room == ROOM_OFFICE:
            if cmd == CMD_WEST:
                print("You enter the Museum Hallway.")
                if flag_tv_on == False:
                    print("The Lights are ON")
                if stella == False:
                    print("Shhhh, there's a police officer around here")
                if stella == True:
                    print("The officer is knocked out... hope he is just knocked out... ")
                room = ROOM_LIVING
                continue

        if room == ROOM_LIVING:
            if cmd == CMD_SOUTH:
                print("You enter the Vault Room")
                if op == True:
                    print("Vault Door is open")
                if op == False:
                    print("Vault Door is closed")
                room = ROOM_KITCHEN
                continue

        if room == ROOM_KITCHEN:
            if cmd == CMD_OPEN:
                if locked == True:
                    print("Vault Door is locked ")
                    continue
                if locked == False:
                    print("Vault Door open")
                    print("There's an access card and a knife")
                    op = True
                    continue

        if room == ROOM_KITCHEN:
            if cmd == CMD_GET:
                if op == True:
                    print("You have the access card and also the knife... for protection...")
                    bone = True
                    continue
                if op == False:
                    print("Vault Door is not open")
                    continue

        if room == ROOM_KITCHEN:
            if cmd == CMD_UNLOCK:
                if key == True:
                    print("Vault Door unlocked")
                    locked = False
                    continue
                if key == False:
                    print("Don't know how to open that")
                    continue

        if room == ROOM_KITCHEN:
            if cmd == CMD_NORTH:
                print("You enter the Museum Hallway.")
                if flag_tv_on == False:
                    print("The Lights are ON")
                if stella == False:
                    print("Shhhh, there's a police officer around here")
                if stella == True:
                    print("The officer is knocked out... hope he is just knocked out... ")
                room = ROOM_LIVING
                continue

        if room == ROOM_LIVING:
            if cmd == CMD_NORTH:
                if stella == False:
                    print("The Police Officer trapped you!")
                    room = ROOM_LIVING
                    break
                if stella == True:
                    print("-Finally, almost there")
                    if flag_tv_on == True:
                        print("It's dark in the hallway")
                    if spamr == True:
                        print("Some secret documents are by a table...")
                        print("-This is it, everyone has to know this")
                    room = ROOM_BED
                    continue

        if room == ROOM_BED:
            if cmd == CMD_BED:
                if flag_tv_on == True:
                    print("Lights are OFF, the Police outside will notice we are here")
                    continue
                elif op == True:
                    print("The Vault is open, we have to close it")
                    continue
                elif key == True:
                    print("The key!!, no one can have it, if the police traps us with the key, we lose it")
                    continue
                elif safe == True:
                    print("The Cryptex is not closed")
                    continue
                elif locked == False:
                    print("The Vault is not locked, anyone can enter")
                    continue
                elif spam == True:
                    print("The documents, we have to put them at the Vault")
                    continue
                elif spamr == True:
                    print("The documents by the table")
                    continue
                print(">> All we wanted was to know the truth and publish it but...")
                print("In this room is buried the body of Maria Magdalene... Jesus wife ")
                print("This means there's a blood line of Jesus which Sophie is part from")
                print("It's all to you, you make it public, or keep it as a secret to ")
                print("protect Sophie")
                space()
                print("You WIN, All the crime scene is resolved")
                break

        if room == ROOM_BED:
            if cmd == CMD_GET:
                if spam == False:
                    print("You got the documents")
                    spam = True
                    spamr = False
                    continue
                if spam == True :
                    print("You already have the documents")
                    continue

        if room == ROOM_LIVING:
            if cmd == CMD_FEED:
                if bone == True and flag_tv_on == False:
                    print("The lights are ON, the officer saw you coming from miles away")
                    print("He arrested you. You LOST")
                    print(turn, "turns played.")
                    return False
                if bone == False:
                    print("You tried to fight the officer bare handed?... He arrested you")
                    print(turn, "turns played.")
                    return False
                if bone == True and flag_tv_on == True:
                    print("You knocked out the officer")
                    stella = True
                    continue

        if room == ROOM_LIVING:
            if cmd == CMD_TV:
                if flag_tv_on == False:
                    print("You turned OFF the lights")
                    flag_tv_on = True
                    continue
                if flag_tv_on == True:
                    print("You turned ON the lights")
                    flag_tv_on = False
                    continue

        if room == ROOM_BED:
            if cmd == CMD_SOUTH:
                print("You enter the Museum Hallway.")
                if flag_tv_on == False:
                    print("The Lights are ON")
                if stella == False:
                    print("Shhhh, there's a police officer around here")
                if stella == True:
                    print("The officer is knocked out... hope he is just knocked out... ")
                room = ROOM_LIVING
                continue

        if room == ROOM_KITCHEN:
            if cmd == CMD_CLOSE:
                if op == True:
                    print("Vault Door closed")
                    op = False
                    continue
                if op == False:
                    print("Vault Door is already closed")
                    continue

        if room == ROOM_KITCHEN:
            if cmd == CMD_LOCK:
                if locked == False:
                    print("Vault Door locked")
                    locked = True
                    continue
                if locked == True:
                    print("Vault Door is already locked")
                    continue

        if room == ROOM_KITCHEN:
            if cmd == CMD_PUT:
                if spam == True and op == True:
                    print("You put the documents in the Vault")
                    spam = False
                    spamr = False
                    continue
                elif op == False:
                    print("Vault Door is closed")
                    continue
                elif spam == False:
                    print("Don't have anything to put in")
                    continue

        print("Illegal command.")

    print(turn, "turns played.")
    return True


Project2()