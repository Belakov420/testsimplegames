secret_word = "Tiger"
guess = ""
guess_count = 0
guess_limit = 2
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Two guesses,hints-carnivore,solitary hunters,weighing up to 300kg: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("No more guesses available, YOU LOST")
else:
     print("CORRECT YOU WIN!")