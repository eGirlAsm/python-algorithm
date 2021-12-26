alpha = ["a","b","c","d"]
#bucket = []		
			
l = len(alpha)					
height = 0
width = 0

r = 0

def add(bucket, baseIndex):
	copy = bucket.copy()
	for x in range(baseIndex+1,l):
		copy.append(alpha[x])
#		print( '+ ->' +  ''.join(copy))
		replace(copy,x)
	copy.clear()
#	print(bucket)
	
def replace(bucket, baseIndex):
	
	for x in range(baseIndex+1,l):
		copy = bucket.copy()
		copy.append(alpha[x])
		print(''.join(copy))
		copy.clear()

def init():
	bucket = []
	for x in range(0,l):
		bucket.append(alpha[x])
		

		print(''.join(bucket))
		replace(bucket,x)
		
		add(bucket, x)
		bucket.clear()
		
init()
#	print(alpha[x])

#for x in range(0,l):
#	print(alpha[x])
#	for y in range(x+1,l):
#		print(alpha[x] + alpha[y])
#		for z in range(y+1,l):
#			print(alpha[x] + alpha[y] + alpha[z])
#			for a in range(z+1,l):
#				print(alpha[x] + alpha[y] + alpha[z] + alpha[a])
#				for b in range(a+1,l):
#					print(alpha[x] + alpha[y] + alpha[z] + alpha[a] + alpha[b])
#					for c in range(b+1,l):
#						print(alpha[x] + alpha[y] + alpha[z] + alpha[a] + alpha[b]+ alpha[c])
#						for d in range(c+1,l):
#							print(alpha[x] + alpha[y] + alpha[z] + alpha[a] + alpha[b]+ alpha[c]+ alpha[d])
	
	
#while width != l:
#	bucket.append(alpha[width])	
#	print(''.join(bucket))
#	for height in range(height,l):
#		# 
#		bucket.append(alpha[height])	
#		print(''.join(bucket))
#		height += 1
#		continue
#	width += 1

#for x in range(0,l):
#	while width != l:
#		bucket.append(alpha[width])
#		print(''.join(bucket))
#		while height != l:
#			bucket.append(alpha[height])
#			print(''.join(bucket))
#			height += 1
#			bucket.clear()
#		width += 1
#	print(f'r = {r}')
	
	
