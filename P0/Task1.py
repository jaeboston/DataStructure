"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
import csv
with open(os.path.join(__location__, 'texts.csv'),'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(os.path.join(__location__,'calls.csv'), 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

#: get all phone numbers in texts
phones = set()
for i in range(len(texts)):
    phones.add(texts[i][0])
    phones.add(texts[i][1])
for i in range(len(calls)):
    phones.add(calls[i][0])
    phones.add(calls[i][1])

print(f"There are {len(phones)} different telephone numbers in the records.")
