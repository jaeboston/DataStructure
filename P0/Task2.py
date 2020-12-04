"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

maxDuration = 0
maxPhone1 = None
maxPhone2 = None
for i in range(len(calls)):
    if int(calls[i][3])> maxDuration:
        maxDuration = int(calls[i][3])
        maxPhone1 = calls[i][0]
        maxPhone2 = calls[i][1]
        

print(f"{maxPhone1} and {maxPhone2}  spent the longest time, {maxDuration} seconds, on the phone during  September 2016.")

#"89071 50880 and (04546)388977 spent the longest time, 4617 seconds, on the phone during  September 2016."