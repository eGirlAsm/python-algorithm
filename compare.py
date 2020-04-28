v1 = ['a','b','c','d','e']

def add_ext(prefix,start_col):
	bucket = []
	for x in range(start_col,len(v1)):
		temp = prefix.copy()
#		if len(bucket) < count:
		if v1[x] not in temp:
			temp.append(v1[x])
			bucket.append(temp)

	return bucket

row = 0
col = 0
while row < len(v1):
	col = row
	temp = []

	temp.append(v1[row])
#		temp.append(v1[row+1])
	while True:
		print(temp)
		r = add_ext(temp,row)
		print(r)
		if not len(r): break
		if (len(r[0]) + row) >= len(v1):
			break

#		print(len(r[0]))
		col += 1
#		print('col',col)
		temp.append(v1[col])

	print('-------------len',len(temp))
#	break
	row += 1
