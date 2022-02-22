import random

#Variables declared and initialized
NUMBER = 10000  #Variable for number of dice rolls

die1Value = 0   #Value of the first die
die2Value = 0   #Value of the second die
count = 0       #Total number of dice rolls
snakeEyes = 0   #Number of snake eyes rolls
twos = 0        #Number of double two rolls
threes = 0      #Number of double three rolls
fours = 0       #Number of double four rolls
fives = 0       #Number of double five rolls
sixes = 0       #Number of double six rolls

#Random number code: var = random.randint(1,6)
while NUMBER > 0:
#for rolls in range(NUMBER):
    NUMBER -= 1
    die1Value = random.randint(1,6)
    die2Value = random.randint(1,6)
    if die1Value == die2Value:
        if die1Value == 1 and die2Value == 1:
            snakeEyes += 1
        elif die1Value == 2 and die2Value == 2:
            twos += 1
        elif die1Value == 3 and die2Value == 3:
            threes += 1
        elif die1Value == 4 and die2Value == 4:
            fours += 1
        elif die1Value == 5 and die2Value == 5:
            fives += 1
        else:
            die1Value == 6 and die2Value == 6
            sixes += 1
    count += 1

#Display the results
print("You rolled snake eyes\t\t", snakeEyes, "out of ", count, " rolls.")
print("You rolled double twos\t\t", twos, "out of ", count, " rolls.")
print("You rolled double threes\t", threes, "out of ", count, " rolls.")
print("You rolled double fours\t\t", fours, "out of ", count, " rolls.")
print("You rolled double fives\t\t", fives, "out of ", count, " rolls.")
print("You rolled double sixes\t\t", sixes, "out of ", count, " rolls.")