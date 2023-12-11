from translate import translate
import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wiktionary.org/wiki/Appendix:1000_basic_English_words')
soup = BeautifulSoup(req.content, features="html.parser")
words = [tag.text for tag in soup.find_all('a') if len(tag.text.split(' ')) == 1 and tag.text!='']


from time import time
start = time()   #### Completed in  438.93

# Loop over the words and place into dictionary with
# english word as key and dictionary containing translations
data = dict()
for word in words:
    word = word.strip()
    translations = translate(word)
    if translations:
        data[word] = translations

end = time()
print(f'Completed in {end-start: 0.2f}')

# Save the translations to out file
import json
with open('dictionary.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)