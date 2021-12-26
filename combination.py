from itertools import *

v5 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"]]
	
	
#v1 = ['a','b','c','d','e']
total = 0
for x in range(0,len(v5)):
	r = combinations(v5,x)
	d = list(r)
	print(d,len(d))
	total += len(d)
	
	
print('total',total)