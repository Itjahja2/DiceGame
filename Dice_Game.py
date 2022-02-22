#Declare variable to quit
#Declare score variable
leaveprogram = 0
score = 0

print("This is a dice rolling game")
#While loop making the game go on forever
while leaveprogram != 'q':
    import random
    random.seed()
    print("Press enter to roll")
    input()
    number = random.randint(1,6)
    score = score + number
    if number == 1:
        print("[-----------]")
        print("[           ]")
        print("[     0     ]")
        print("[           ]")
        print("[-----------]")
        print(' ')
        print('your score: ',score )
        print("Type 'q' to quit")
        leaveprogram = input()
    elif number == 2:
        print("[-----------]")
        print("[  0        ]")
        print("[           ]")
        print("[        0  ]")
        print("[-----------]")
        print(' ')
        print('your score: ',score )
        print("Type 'q' to quit")
        leaveprogram = input()
    elif number == 3:
        print("[-----------]")
        print("[  0        ]")
        print("[     0     ]")
        print("[        0  ]")
        print("[-----------]")
        print(' ')
        print('your score: ',score )
        print("Type 'q' to quit")
        leaveprogram = input()
    elif number == 4:
        print("[-----------]")
        print("[  0     0  ]")
        print("[           ]")
        print("[  0     0  ]")
        print("[-----------]")
        print(' ')
        print('your score: ',score )
        print("Type 'q' to quit")
        leaveprogram = input()
    elif number == 5:
        print("[-----------]")
        print("[  0     0  ]")
        print("[     0     ]")
        print("[  0     0  ]")
        print("[-----------]")
        print(' ')
        print('your score: ',score )
        print("Type 'q' to quit")
        leaveprogram = input()
    elif number == 6:
        print("[-----------]")
        print("[  0  0  0  ]")
        print("[           ]")
        print("[  0  0  0  ]")
        print("[-----------]")
        print(' ')
        print('your score: ',score )
        print("Type 'q' to quit")
        leaveprogram = input()
    #Ending the game if the user presses 'q'
    if leaveprogram == 'q' or leaveprogram == 'Q':
        print("Ending dice game... \nSee you next time.")