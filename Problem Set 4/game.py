from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

random_number = randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    
    if guess < 1:
        pass
    elif guess < random_number:
        print("Too small!")
    elif guess > random_number:
        print("Too large!")
    else:
        print("Just right!")
        break
