import string
import re
import sys

if len(sys.argv) < 2:
    print('Usage: <PYTHON_CMD> count_words.py <FILEPATH>')
    exit()

FILEPATH = sys.argv[1]


try:
    fhand = open(FILEPATH)
except:
    print('Error opening file ', FILEPATH)
    exit()

results = dict()

for line in fhand:
    line.strip().translate(line.maketrans('', '', string.punctuation))
    words = re.findall('\S+', line)
    for word in words:
        word = word.strip().lower()
        results[word] = results.get(word, 0) + 1

for key, val in list(results.items()):
    print(val, key)
    
    
