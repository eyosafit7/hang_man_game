import random 

print(" ")
print("---------- HANG_MAN_GAME -----------")
print(" ")


def draw_img(life):
    print("       ----    ")
    print("       |   |   ")

    if life < 6:
        print("       0   |   ")
    else:
        print("           |   ")

    if life < 3:
        print("      /|\\  |   ")
    elif life < 4:
        print("      /|   |   ")
    elif life < 5:
        print("       |   |   ")
    else:
        print("           |   ")

    if life < 1:
        print("      / \\  |   ")
    elif life < 2:
        print("      /    |   ")
    else:
        print("           |   ")

    print("           |   ")

def search(words,word):
    count = 0
    for i in range(len(words)):
        if words[i] == word:
            char_gotten[i] = words[i]
            count += 1
    return count


random_words = ["juice","puppy","happy","animation","bored","lemon","cycle",
                "buddy","fruit","sleep","art","python","cry","help","question",
                "zebra","lion","tiger","anger","barber","safe","game","hair",
                "bucket","graph","subject","television","tiktok","code","program"]
guess_words = random.choice(random_words)
left_life = 6
char_gotten = ["_"] * len(guess_words)
gotten = []
missed = []
draw_img(left_life)

while left_life > 0 and "_" in char_gotten:
    print(f"guess the word: {" ".join(char_gotten)}")
    user_data = input("guess a character: ").lower()

    if user_data == "quit":
        break
    if len(user_data) == 1 and user_data.isalpha():
        count = search(guess_words,user_data)

        if count > 0:
            if user_data in gotten:
                print(f"do not repeat {user_data} you already got it!")
            else:
                print(f"you got {count}({user_data})!")
                gotten.append(user_data)
        else:
            if user_data not in missed:
                left_life -= 1
                print(f"you missed, {left_life} life left!")
                missed.append(user_data)
            else:
                print(f"you already typed {user_data} and failed")
        print("---------------    ---------------")
        draw_img(left_life)
        print(" ")
    else:
        print(f"{user_data} is not valid, type one letter only")

if "_" not in char_gotten:
    print("you won!")
else:
    print(f"you lost!")
    
print(f"the word was {guess_words}")
print(" ")



