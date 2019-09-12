import json
import sys

#initial setup

number_letters = int(input("How many letters your word have?\n"))
using_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = []

#load json file

try:

    with open('./words/{}-letter.json'.format(number_letters)) as f:
        json = json.load(f)
        for w in json:
            words.append(w['word'])

except:
    
    sys.exit('No json file with {} letters'.format(number_letters))

#start

##check which letters will use to guess
for a in using_alphabet:
    has = False

    for w in words:
        if a in w:
            has = True
            break

    if not(has):
        using_alphabet.remove(a)

##function to update the letters and words
def dontHave( letter ):
    global words
    global using_alphabet

    using_alphabet.remove(letter)
    
    new_words = []
    for w in words:
        if not(letter in w):
            new_words.append(w)
    
    words = new_words


dontHave('a')
print(using_alphabet)
print(words)