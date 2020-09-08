"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('p0/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('p0/P0/calls.csv', 'r') as f:
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
number=0
duration=0

for i in calls:
    if i[2][3:10]=='09-2016' and int(i[3])>int(duration):
        duration=i[3]
        number=i[0]
print(number,"spent the longest time,",duration,"seconds, on the phone during September 2016.")    
    
