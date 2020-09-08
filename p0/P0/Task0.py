"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('/home/darshan/Desktop/DSA Nanodegree/p0/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/home/darshan/Desktop/DSA Nanodegree/p0/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
print("First record of texts,", texts[0][0]," texts ", texts[0][1]," at time ",texts[0][2][-8:])

print("Last record of calls,",calls[0][0]," callls ",calls[0][1], "at time ", calls[0][2][-8:], " lasting ",calls[0][3])


