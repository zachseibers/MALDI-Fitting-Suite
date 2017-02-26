'''
The purpose of this program is to calculate molecular mass from chemical 
formulas...to be extended to a function to calculate repeat unit mass for polymers.
'''

import re
from elements import elements

formula = 'SC10H14'
parser = '[A-Z][a-z]?\d*'

breakdown = re.findall(parser, formula)
print(breakdown)

symbolparser = "[A-Z][a-z]?"
numberparser = "\d*"
weight=[]

for e in breakdown:
    symbol = re.findall(symbolparser, e)
    print(symbol)
    number = re.findall(numberparser, e)
    print(number)
    if number [1]:
        print(number)
        weight.append(elements()[symbol[0]] * int(number[1]))
    else:
        weight.append(elements()[symbol[0]])
        
print(weight)
print(sum(weight))