import re
s = '8C3721D86'
r = re.match('\d',s)
print(r)
r1 = re.search('\d',s)
print(r1)
r2 = re.findall('\d',s)
print(r2)