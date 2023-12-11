import json
from random import randint

with open('dictionary.json', 'r') as f:
    words = json.load(f)

while True:
    print('What is the translation of', end=': ')

    word_data = list(words.items())
    random_word = randint(0, len(words)-1)
    en_word = word_data[random_word]
    translations = list(en_word[1].items())
    random_question = randint(0, len(en_word[1])-1)
    question = translations[random_question]
    print(question[0])
    answer = input('What is the english translation: ')
    print(question[1]['en'])
    print('-'*35)
    print()
    # # if answer not in question['en']:
    # #     print("Wrong!")
    # print("Correct!")