

secret_word = "Playstation"
guess = ""
guess_count = 0
guess_limit = 3
ofg = False

while guess != secret_word and not ofg:
    if guess_count < guess_limit:
        guess = input("Please enter the secret word: ")
        guess_count += 1
    else:
        ofg = True


if ofg:
    print("You Lose")
else:
    print("You win")
