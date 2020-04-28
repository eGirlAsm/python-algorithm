
from itertools import *
v1 = ['a','b','c','d']
v2 = [1,2,3,4]
#a = accumulate(v2)
#print(list(a))
#print(list(zip_longest(v1,v2)))
print(len(list(combinations(v1, 4))))
#g_count = 2
#
#def getList(nStart):
#	list = []
#	# satisfy the length
#	count = len(v1) - nStart
#	if count < g_count:
#		return False
#	else:
#		for x in range(nStart,len(v1)):
#			list.append(v1[x])	
#	
#	return list
#	
#bucket = []

#def recursive(index, baseData, nRepeat, temp_bucket):
#	for x in range(index,len(v1)):
#		if nRepeat < 2:
#			print(v1[x],nRepeat)
#			temp_bucket.append(v1[x])
##			print(temp_bucket)
#			recursive(x+1, nRepeat+1,temp_bucket)
#		else:
#			print('enenenennenenddddd-')
#			print(temp_bucket)
#			break
		
		
#		while 
#		
#		print('recursive',getList(x))
		

#for x in range(0,len(v1)):
#	temp = []
#	recursive(x ,v1[x], 0, [])
	

#def recursion(data, index, bucket):
#	for x in range(index,len(data)):
#		print(data[x],index)
#		bucket.append(data[x])
##		recursion(data, index+1, bucket)
#		
#	return bucket

#def compare(data,count):
#	bucket = []
#	for x in range(0,len(data)):
##		bucket.append([].append(x))
#		line_bucket = []
#		bucket.append(data[x])
#		print('head > ',data[x])
#		tail_data = recursion(data, x+1, [])
#		print(list(zip(data[x],tail_data)))
#		line_bucket.append(tail_data)
#		bucket.append(line_bucket)
#		print('tail_data',tail_data)
##		for y in range(x+1,len(data)):
##			print(data[x],data[y])
#	
#	return bucket	
#	
#data = compare(v1, 2)
##print(data)
#list_one = ['Joe', 'Mark', 'Jane']
#list_two = [ 100, 34, 87, 23, 65 ]
#merged2 = zip(cycle(list_one), list_two)
#print(list(merged2))
#print(list(cycle(list_one)))
#print(list(merged2))
#x = zip(cycle('abcd'),'xy')
#print(list(x))

#for x in range(0,len(v1)):
#	cb = zip(v1[x])
