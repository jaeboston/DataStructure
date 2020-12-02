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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
fromBang = []
toFixed = []
toBang = []
toMobile = []
toTele = []
areacode = set()

for call in calls:
  if call[0].startswith('(080)'):
    fromBang.append(call)
    if call[1].startswith('(0'):
      toFixed.append(call)
      #: add the area code to the set
      close_paren_index = call[1].index(')')
      areacode.add(call[1][1:close_paren_index])
      
      if call[1].startswith('(080)'):
        toBang.append(call)
    if call[1].startswith('7') or call[1].startswith('8') or call[1].startswith('9'):
      toMobile.append(call)
    if call[1].startswith('140'):
      toTele.append(call)

#: sort areacode
sorted_areacode = sorted(areacode)
print("The numbers called by people in Bangalore have codes:")
print(sorted_areacode)

print(f"{len(toBang)/len(toFixed)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
