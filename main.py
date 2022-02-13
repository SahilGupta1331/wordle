import os
import random
from urllib import request
import itertools

if not os.path.isfile('count_1w.txt'):
    request.urlretrieve(
        "https://norvig.com/ngrams/count_1w.txt",
        "count_1w.txt")

with open('count_1w.txt') as file:
    five_letter_words = list(itertools.islice((
        word for word, _ in (line.strip().split('\t') for line in file)
        if len(word) == 5), 10000))

word = random.choice(five_letter_words)
t = 5

while True:
    if t == 0:
        print('You lost. Better luck next time!')
        print('The word was ', word)
        break
    j = 0
    guess = input('Guess the 5 letter word: ')
    if guess == word:
        print('🟩🟩🟩🟩🟩')
        print('You Won!!!')
        break
    elif len(guess) == 5:
        grid = {i: '⬛' for i in range(5)}
        count = {i: 0 for i in set(guess)}
        for i in guess:
            count[i] += 1
            if i == word[j]:
                grid[j] = '🟩'
            elif i in word and word.count(i) >= count[i]:
                grid[j] = '🟨'
            j += 1
        print(''.join(grid.values()))
        t -= 1
    else:
        print('Give a valid 5 letter word.')
    print('Total chances left: ', t)
