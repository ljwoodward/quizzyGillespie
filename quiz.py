from ui import opening
import requests

url = 'https://opentdb.com/api.php?amount=10'
categoryUrl = 'https://opentdb.com/api_category.php'
categoryCountUrl = 'https://opentdb.com/api_count.php?category=CATEGORY_ID_HERE'
globalCountUrl = 'https://opentdb.com/api_count_global.php'
exampleUrl = 'https://opentdb.com/api.php?amount=<AMOUNT>&category=<CATEGORY>&difficulty=<DIFFICULTY?&type=<QUESION_TYPE>'
#
# CONSTANTS
#

# API keys
DIF = 'difficulty'
QU = 'question'
TYP = 'type'
CA = 'correct_answer'
IA = 'incorrect_answers'

#


def generate_url(options):
    pass



def decode(text):
    return text.replace('&quot;', '').replace('&#039;', '\'')

opening()
response = requests.get(url)
json = response.json()
results = json['results']
for i in results:
    question = decode(i[QU])
    options = [decode(j) for j in i[IA]]
    options.append(decode(i[CA]))
    options.sort()
    print(question)
    for j in range(len(options)):
        print(f'{j}. {options[j]}')
    answ = input('Answer: ')
    cor = decode(i[CA])

    anlen = len(answ)
    if int(answ) == options.index(cor):
        print(cor)
        print('correct')
    else: print(f'no, the answer was {cor}')
