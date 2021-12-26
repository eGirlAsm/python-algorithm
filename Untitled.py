v1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
v2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
v3 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["green_turban", "headgear"], ["blue_sunglasses1111", "eyewear"],["yellow_hat", "headgear"]]
bucket = []
y = 0
z = 0

def match_all(clothes, index, length):
	matched = 0
	print(f'length = {length}')
	overcount = 0
	
	temp_bucket = []
	temp_bucket.append(clothes[index])
	
	for x in range(index + 1,len(clothes)):
		while len(temp_bucket) < length:
			if clothes[x][1] not in [item[1] for item in temp_bucket]:
				temp_bucket.append(clothes[x])
				print(temp_bucket)

#		print(len(temp_bucket))
#		print(temp_bucket)
			overcount += 1
			if overcount > 100:
				print('overcouted')
				break
#	for x in range(index + 1,len(clothes)):
#		temp_bucket = []
#		temp_bucket.append(clothes[index])
#		if clothes[x][1] not in [item[1] for item in temp_bucket]:
#			while len(temp_bucket) < length:
#				for y in range(index+1,len(clothes)):
#				if clothes[x][1] not in [item[1] for item in temp_bucket]:
#					temp_bucket.append(clothes[x])		
					
					
					
#				overcount += 1
#				if overcount > 100:
#					print('overcouted')
#					break
#			print(len(temp_bucket))
#			if len(temp_bucket) < length:
#				temp_bucket.append(clothes[x])
#	#			print(f'+appended {clothes[x]}')
#			print(temp_bucket)
#			else:
#				temp_bucket.clear()
#	print(f'length = {length}')
#	print(f'matched = {matched}')
	return matched
hash_table = []

def solution(clothes):
	overcount = 0
	answer = 0
	l = len(clothes)
	print(f'len = {l}')
	x = 0
	repeat = 0
	index = 0
#	clothes = sorted(clothes)
#	
	for g_x in clothes:
		print(g_x)
		while True:
			bucket.append(clothes[x])
			x += 1
			if(x == l):
				print('============end==============')
				bucket.clear()
				x = 0
				repeat += 1
				continue
			
			if repeat == l:
				print(f'{repeat} count repeated')
				break
#	while True:
##		print(f'will apppend index = {x} data = {clothes[x]}'))
#		base = clothes[x]
#		
#		bucket.append(clothes[x])
#		answer += 1
#		print(bucket)
#		
#		x += 1
#		if(x == l):
#			print('============end==============')
#			bucket.clear()
#			x = 0
#			repeat += 1
#			continue
#		
#		
#		if repeat == l:
#			print(f'{repeat} count repeated')
#			break
#			
#	print(f"matched {answer} times")
#	for x in range(0,l):
#		print(f'x = {clothes[x]}')
#		for y in range(0,l):
#			print(f'x = {clothes[x]} y = {clothes[y]}')
#			for z in range(0,l):
#				print(f'x = {clothes[x]} y = {clothes[y]} z = {clothes[z]}')
#		bucket.append(clothes[x])
#		print(f'{bucket}')
#		answer += 1
		
#		for how_long in range(2,l):
#			r = match_all(clothes, x, how_long)
#			answer += r
#		y = x + 1
#		while y != l:
#			# check type already in 
##			print(f'y = {y} , will append {clothes[y]}')
#			if clothes[y] not in bucket:
##				print(f'searching type "{clothes[y][1]}" in bucket = {bucket}')
#				if clothes[y][1] not in [item[1] for item in bucket]:
#					bucket.append(clothes[y])
#					print(f'y bucket = {bucket}')
##					print(f'bucket appended = {bucket}')
#					answer += 1
##				else:
###					print(f'already has type but check different name then replace')
##					if clothes[y][0] not in [item[0] for item in bucket]:
##						for item in bucket:
###							print(clothes[y][0])
###							print(f'item1 => {item[1]} == item2 =>{clothes[y][1]} ')
##							if item[1] == clothes[y][1]:
###								print(f'okokkooo = ')
##								bucket.remove(item) 
##						bucket.append(clothes[y])
##						print(f'z = bucket = {bucket}')
###						print(f'bucket replaced = {bucket}')
##						answer += 1
#					
##			z = y + 1
#			z = 0
#			while z != l:
##				print(f'z = {z} , will append {clothes[z]}')
#				if clothes[z][1] not in bucket:
##					print(f'searching type "{clothes[z][1]}" in bucket = {bucket}')
#					if clothes[z][1] not in [item[1] for item in bucket]:
#						bucket.append(clothes[z])
#						print(f'z = bucket = {bucket}')
##						print(f'bucket appended = {bucket}')
#						answer += 1
##					else:
###						print(f'already has type but check different name then replace')
##						if clothes[z][0] not in [item[0] for item in bucket]:
##							for item in bucket:
##	#							print(clothes[y][0])
###								print(f'item1 => {item[1]} == item2 =>{clothes[z][1]} ')
##								if item[1] == clothes[y][1]:
##	#								print(f'okokkooo = ')
##									bucket.remove(item) 
##							bucket.append(clothes[z])
##							print(f'bucket = {bucket}')
###							print(f'bucket replaced = {bucket}')
##							answer += 1
#				z += 1
#			
#			break
#		print(f'---------------- x - downdown {bucket} --------------------')
#		bucket.clear()
	return answer
	
#print('result = ' +  str(solution(v1)))
#print('result = ' +  str(solution(v2)))
print('result = ' +  str(solution(v3)))