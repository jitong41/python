#组
import re
a ='pythonC#JavaC#'

def convert(value):
    matched = value.group()
    return '!!'+matched+'!!'

r= re.sub('C#',convert,a)
print(r)

