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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

fromCallTele = set()
toCallTele = set()
fromTextTele = set()
toTextTele = set()

for call in calls:
    if call[0].startswith('140'):
        fromCallTele.add(call[0])
    if call[1].startswith('140'):
        toCallTele.add(call[1])

for text in texts:
    if text[0].startswith('140'):
        fromTextTele.add(text[0])
    if text[1].startswith('140'):
        toTextTele.add(text[1])

for number in fromCallTele:
    if number in toCallTele or number in fromTextTele or number in toTextTele:
        fromTextTele.remove(number)

sorted_fromCallTele = sorted(fromCallTele) 

print(f"These numbers could be telemarketers: ")
print(sorted_fromCallTele)
