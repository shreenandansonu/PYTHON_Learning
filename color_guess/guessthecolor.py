from color_guess_main import *

color_list=["R","G","B","V","Y","O","W"]
sequence=generate_color()
num_guess=1
while True:
    print("You have to choose colors from ",color_list)
    guess=input("Enter Your Guess: ")
    if(check_sequence(sequence,guess)[2]):
        print("🎉✅Correct Guess🎉")
        print(f"You guessed in {num_guess} guess.")
        break
    else:
        print(f"Correct: {check_sequence(sequence,guess)[0]}, Incorrect: {check_sequence(sequence,guess)[1]}")
        num_guess+=1
