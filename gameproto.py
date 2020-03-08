# game prototype

print('You wake up. Your head is pounding.Then you hear a metallic voice."Passenger 325 wake up!')
print('You cough. You barely manage to open your eyelids. The light is blidning you;')
print('"Passenger 325 wake up! You are on a spaceship Canaveral and your immidiate assistance is needed!"')
print('You shake your head and say: "I have a name! I am not a number"')
print('Metallic voice asks:"What is your name then..?"')
myName = input()
print('Glad you are awake, ' + myName)
print('Do you know where you are ' + myName + ' ? (yes/no)')
locationAnswer = input()
required_inputs = ['yes','no']

while locationAnswer.lower() not in required_inputs:
    print("Sorry didn't catch that.")
    print("Do you know where you are? (yes/no)")
    locationAnswer = input()

if locationAnswer.lower() == 'yes':
    print('Good, so you know you are on a spaceship. We are travelling at the  0,3 of lightspeed and we just passed Ooort Cloud')

elif locationAnswer.lower() == 'no':
    print('I told you already. You are in the spaceship Canaveral. We are travelling at the  0,3 of lightspeed and we just passed Ooort Cloud')

print('You look around and you see that you are in a large chamber surrounded by sleeping pods. Exactly same ones as the one you are in.')
print('"Hold on I will release youfrom your sleeping pod. You have been in cryogenic sleep for over 10 years. It might feel shaky a bit"')
print('"RELEASING PASSENGER 325. NAME ' + myName + ' "')
print('You feel a sudden gust of cold air, as the pods gate opens and your body hits the floor. You get up on your feet, you find yourself naked and shaking of cold')
print('The metallic voice says" On the left is locker with your things. You have to enter the code to open it. The code is 1212 ')
print('You come towards the locker. The touchscreen next to the lock displays: ENTER THE CODE:')
LockerCode = input()
required_code = ['1212']

while LockerCode not in required_code:
    print('Wrong code! Try again.')
    LockerCode = input()
if LockerCode == '1212':
    print('ACCESS GRANTED. The locker opens.')
print('In the locker you find a suit, which you immidiately put on yourself. You also find a portable computer, a medkit and a laser pistol.')
print('You cannot carry all the things with you. You can only take one of them. Which item do you choose? (computer/medkit/pistol)')
 
EquipmentTaken = input()
required_inputs = ['medkit','computer','pistol']

while EquipmentTaken.lower() not in required_inputs:
    print('Wrong asnwer. You need to specify ONE item you wish to take(computer/medkit/pistol)')
    EquipmentTaken = input()
    
if EquipmentTaken.lower() in required_inputs:
    print('You choose '+ EquipmentTaken + ' to take with you.')

print('Hopefully you will not regret that choice.')

print('You exit the room with ' + EquipmentTaken + ' in your hand. It is time to get to know what happened here and why the ships AI woke you up.')
print('"Computer!" you say. "Tell me what is the status of the flight')
print('Metallic voice of the starships computer answers "Our flight is endangered, we are off course. This is why I woke you up. You need to reach navigation room and correct the course of the ship. Otherwise we will fly into a blackhole"')
print('You ask the computer "How do I get there?"')
print('"You can either take a shuttle, it will be faster but the shuttle system might be malfunctioning. Or you can go through the ventilation shaft, it is longer way and can be dangerous"')
print('Which path do you take? (shuttle/ventilation shaft)')

PathTaken = input()
required_inputs = ['shuttle','ventilation shaft']

while PathTaken.lower() not in required_inputs:
    print('Wrong answer. You need to specify which path you take (shuttle/ventilation shaft)')
    PathTaken = input()
    
if PathTaken.lower() == 'shuttle':
    print('You decide to take a  '+ PathTaken)
    print('You step into the shuttle and the glass door closes behind you. You tap "Navigation room" on the panel and the shuttle launches.')
    print(' Few minutes into the ride a alarm goes off. The screen shows CRITICAL ISSUE. You need a computer to connect to shuttles system and fix it.')
    if EquipmentTaken.lower() == 'computer':
        print('Luckily you took the computer with you, so you plug it in')
        print('The screen shows "What would you like to do? (REBOOT/CANCEL/WATCH NETFLIX)')
        print('Type in your command:')
        Command = input()
        required_command = ['reboot']
        while Command.lower() not in required_command:
                print('Nothing happens. Then the shuttles breaks malfunction and it crashes full speed into the wall at the end station.')
                print('YOU DIE, STUPID. GAME OVER')
                quit()
        if Command.lower() == 'reboot':
                print('You succesfully reboot the system. The shuttle takes you safely to the navigation room.')
    else:
        print('Unfortunately you did not take the computer with you')
        print('The shuttles breaks malfunction and it crashes full speed into the wall at the end station.')
        print('YOU DIE, STUPID. GAME OVER')
        quit()
        
elif PathTaken.lower() == 'ventilation shaft':
        print('You decide not to trust the shuttle system and take the longer path. You step into ventilation shaft.')
        print('It is dark and claustrophobic. It feels like ages as you crawl through the ventilation system.')
        print('Suddenly you stop. Something is moving in the darkness!')
        print('You see a pair of red glowing eyes approaching you. Then there is a deep growl.')
        print('It is some kind of a nightmarish creature crawling towards you!')
        print('You can try to escape or fight it? What do you do? (escape/fight)')
        
        EncounterChoice = input()
        required_choice = ['escape','fight']

        while EncounterChoice.lower() not in required_choice:
            print('You have only two choices. What do you do? (escape/fight)')
            EncounterChoice = input()
    
        if EncounterChoice.lower() == 'escape':
            print('You decide to run away!')
            print('You turn rapidly and crawl back as fast as you can.')
            print('There is a sudden hassle behind you but you can already see the light of the exit!')
            print('Then something grabs your feet and pulls you into the darkness. You feel sharp teeth digging into your neck. Something wet and warm splashes on your face. It is your blood')
            print('The monster ate you and you die.')
            print('GAME OVER')
            quit()
        elif EncounterChoice.lower() == 'fight' and EquipmentTaken.lower() == 'pistol':
            print('You decide to face the monster and fight for your life.')
            print('Luckily you took that pistol with you.')
            print('You aim directly at creatures ugly face and fire!')
            print('BAM! The creature howls and dies.')
            print('The path is clear now. You succesfully reach the navigation room')
            
        elif EncounterChoice.lower() == 'fight'and EquipmentTaken.lower() is not 'pistol':
            print('You decide to face the monster and fight for your life.')
            print('However you do not have any weapon with you. You should have taken that pistol with you dumb ass.')
            print('You try to punch the monster in the face but it deflects your fist and lunges at you.')
            print('You feel sharp teeth digging into your neck. Something wet and warm splashes on your face. It is your blood!')
            print('The monster ate you and you die.')
            print('GAME OVER')
            quit()
        
print('Finally you arrive at the navigation room')
print('The metallic voice of the ships AI welcomes you "Well done "' + myName + ' " I am glad you made it so far!"')
print('"Now all you have to do is reourate our ship to the new destination."')
print('You come closer to the navigation console and activate it. A gigantic three dimensional hologram with a starmap appears.')
print('"Where would you like to go now?"')
newDestination = input()
print('"Great!"')
print('Ship trembles as its engines adjust to take on the new destination.')
print('"Buckle up! We are now heading towards ' + newDestination)
print('THE END')
      





