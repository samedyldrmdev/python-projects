import random

number = random.randint(1,100)
def number_guess_game():
    selected = int(input("Enter any number: "))

    if selected > number:
        return "Reduce the number! "
        selected = int(input("Enter any number: "))
    elif selected < number:
        return "Increase the number!"
    else:
        return "Congratz! You've won the number guessing game!"

while True:
    print(number_guess_game())



