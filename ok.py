v1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
v2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
v3 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["green_turban", "headgear"], ["blue_sunglasses1111", "eyewear"],["yellow_hat", "headgear"]]

alpha = sorted(v3)

all_matched = []

bucket = []	
	
				
height = 0
width = 0

l = len(alpha)	

for x in range(0,l):
	bucket.append(alpha[x])
	if sorted( [item[0] for item in bucket]) not in all_matched:
		all_matched.append(sorted( [item[0] for item in bucket]) )
	
	print(f'all {all_matched}')
#	hash_table.append(hash(''.join(bucket)))
#	print(hash_table)
	print(bucket)
	while height != l:
#		print(f'will apend {alpha[height]}')
#		print([item[1] for item in bucket])
		if alpha[height][1] not in [item[1] for item in bucket]:
			bucket.append(alpha[height])
			if sorted( [item[0] for item in bucket]) not in all_matched:
				all_matched.append(sorted( [item[0] for item in bucket] ))
			print(bucket)
		else:
#			print("passed")
			pass
		height += 1
	height = 0
	bucket.clear()
	print(f"{x} step  end--------------")
	
	
print("final")
print(all_matched)
print(len(all_matched))
for ok in all_matched:
	print(ok)
#		width = height + 1
#		while width != l:
#			if alpha[width][1] not in [item[1] for item in alpha]:
#				bucket.append(alpha[width])
#				print(bucket)
#
#			width += 1
#		bucket.clear()
#		break