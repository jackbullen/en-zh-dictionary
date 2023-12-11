import requests
from bs4 import BeautifulSoup

def is_chinese_char(char):
    if 0x4E00 <= ord(char) <= 0x9FA5:
        return True
    else:
        return False

def translate(word):
    BASE = 'https://mdbg.net/chinese/dictionary?wdqb='
    url = BASE + word
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        soup_text = soup.find('table', class_='wordresults').find_all('tr')
        soup_translations = filter(lambda x: x!=[] and x!=[''], map(lambda x: [y.text for y in x.find_all('td')], soup_text))
        translations = dict()
        for t, eg, en, level in soup_translations:
            chinese = ''
            for i, char in enumerate(t):
                if is_chinese_char(char):
                    chinese += char
                    continue
                else:
                    break
            pinyin = t[i:]
            translations[chinese] = {
                'pinyin': pinyin.replace('\u200b', ''),
                'eg': eg,
                'en': en,
                'level': level
            }
        return translations
    except AttributeError:
        return