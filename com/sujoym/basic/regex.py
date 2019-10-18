import re
exString = 'Jess is 1015 years old.Tom is 80 years old.Tim is 5 years old and his aunt Amy, is 108.'

ages = re.findall(r'\d{1,4}',exString)
names = re.findall(r'[A-Z][a-z]*',exString)

#print(ages)
#print(names)

agedict = {}
n=0
for x in names:
    agedict[x]=ages[n]
    n+=1

print(agedict)