import os
import random
from urllib import request

if not os.path.isfile("sgb-words.txt"):
    request.urlretrieve(
        "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt", "sgb-words.txt"
    )

with open("sgb-words.txt") as word_list:
    five_letter_words = word_list.readlines()

word = random.choice(five_letter_words)
total_chances_left = 5

while True:
    if total_chances_left == 0:
        print("You lost. Better luck next time!")
        print(f"The word was {word}")
        break
    j = 0
    guess = input("Guess the 5 letter word: ")
    if guess == word:
        print("🟩🟩🟩🟩🟩")
        print("You Won!!!")
        break
    elif len(guess) == 5:
        grid = {i: "⬛" for i in range(5)}
        count = {i: 0 for i in set(guess)}
        for i in guess:
            count[i] += 1
            if i == word[j]:
                grid[j] = "🟩"
            elif i in word and word.count(i) >= count[i]:
                grid[j] = "🟨"
            j += 1
        print("".join(grid.values()))
        total_chances_left -= 1
    else:
        print("Give a valid 5 letter word.")
    print(f"Total chances left: {total_chances_left}")
