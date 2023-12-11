from translate import translate

# Get the words from dwyl/english-words.git repo
with open('words.txt', 'r') as f:
    words = f.readlines()

from time import time
start = time()

# Loop over the words and place into dictionary with
# english word as key and dictionary containing translations
data = dict()
for word in words:
    word = word.strip()
    translations = translate(word)
    if translations:
        data[word] = translations

end = time()
print(end-start)

# Save the translations to out file
import json
with open('dictionary.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)