"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('p0/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('p0/P0/calls.csv', 'r') as f:
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
"""
print(calls[0])
numbers = {}
for i in calls:
  if i[0][:5] == '(080)':
    x=re.match("^\(.*\)",i[1])
    if x:
      numbers[i[1][x.start()+1:x.end()-1]] = None
    else:
        numbers[i[1][:4]] = None

numList = list(numbers.keys())
numList.sort()
print("The numbers called by people in Bangalore have codes:")
for i in numList:
  print(i)


""""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
totalBangloreNumbers = 0
calledToBangloreNumbers = 0
for i in calls:
  if i[0][:5] == '(080)':
    totalBangloreNumbers += 1
    if i[1][:5] == '(080)':
      calledToBangloreNumbers += 1
per = calledToBangloreNumbers / totalBangloreNumbers * 100
print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."%per)