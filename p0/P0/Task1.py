"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('p0/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('p0/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniqueList = []

for i in range(len(texts)):
    if texts[i][0] not in uniqueList:
        uniqueList.append(texts[i][0])
    
    if texts[i][1] not in uniqueList:
        uniqueList.append(texts[i][1])

for i in range(len(calls)):
    if texts[i][0] not in uniqueList:
        uniqueList.append(calls[i][0])
    
    if texts[i][1] not in uniqueList:
        uniqueList.append(calls[i][1])  
print("There are", len(uniqueList), "different telephone numbers in the records.")