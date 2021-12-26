
v1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
v2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
v3 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"], ["h", "father"]]
v4 = [["a", "face"], ["b", "face"], ["c", "face"], ["d", "headgear"], ["e", "headgear"], ["f", "headgear"], ["g", "headgear"], ["h", "headgeara"], ["i", "headgearb"], ["j", "headgearasdf"], ["k", "headgearc"], ["l", "headgeard"], ["m", "headgeare"], ["n", "headgearf"], ["o", "headgear"], ["p", "headgear"], ["q", "headgear"], ["r", "headgear"], ["s", "headgearfda"], ["t", "headgearsd"], ["u", "headgearfd"], ["v", "headgearasdf"], ["w", "headgearfdf"], ["x", "headgearaaa"], ["y", "headgear"], ["z", "headgear"], ["aa", "headgear"], ["bb", "headgearsdsd"], ["cc", "headgear"], ["dd", "headgear"], ["ee", "headgear"], ["ff", "headgear"], ["gg", "headgearasdf"], ["hh", "headgearfda"], ["ii", "headgear"], ["jj", "headgear"], ["kk", "headgear"]]
#v4 = [["a", "face"], ["b", "face"], ["c", "face"], ["d", "headgear"], ["e", "headgear"], ["f", "headgear"], ["g", "headgear"]]
#alpha = ["a","b","c","d","e","f","g"]


def add(all_matched, clothes, bucket, baseIndex):
	copy = bucket.copy()
	for x in range(baseIndex+1,len(clothes)):
		if clothes[x][1] not in [item[1] for item in copy]:
			copy.append(clothes[x])
#			print('^^^<-appended')
#			all_matched.append(sorted( [item[0] for item in copy]) )
#		print( '+ ->' +  ''.join(copy))
		replace(all_matched, clothes, copy,x)
	copy.clear()
	
def replace(all_matched, clothes, bucket, baseIndex, Repeat = False):
	for x in range(baseIndex+1,len(clothes)):
		if Repeat is False:
			copy = bucket.copy()
			print(f'copy => {copy} append-> {clothes[x]}')
			if clothes[x][1] not in [item[1] for item in copy]:
	#			print(f' sorted {sorted( [item[0] for item in copy])}  all_match = {all_matched}')
				copy.append(clothes[x])
				clothes_names = [item[0] for item in copy]
				if clothes_names not in all_matched:
					print('^^^<-appended')
					all_matched.append(clothes_names )
					print(copy)
					print(f'baseIndex = {baseIndex} , x = {x}')
					replace(all_matched, clothes, copy, x, True)
		else:
#			print(f'copy => {copy} append-> {clothes[x]}')
			if clothes[x][1] not in [item[1] for item in bucket]:
	#			print(f' sorted {sorted( [item[0] for item in copy])}  all_match = {all_matched}')
				bucket.append(clothes[x])
				clothes_names = [item[0] for item in bucket]
				if clothes_names not in all_matched:
					all_matched.append(clothes_names )
					replace(all_matched, clothes, bucket, x, True)	
	
#		copy.clear()
		

def solution(clothes):
	bucket = []
	all_matched = []
	answer = 0

#	if len(clothes) < 30:
	clothes = sorted(clothes)
	for x in range(0,len(clothes)):
		bucket.append(clothes[x])
#		print(bucket)
#		if clothes[x][1] not in [item[1] for item in bucket]:
#		if sorted( [item[0] for item in bucket]) not in all_matched:
		all_matched.append( [item[0] for item in bucket] )
			
		replace(all_matched, clothes, bucket, x)
#		break
		
		add(all_matched, clothes, bucket, x)
		bucket.clear()
		
#	print(f'all ------------ --------\n ')
	for x in all_matched:
		print(' + '.join(x))	
	answer = len(all_matched)
	all_matched.clear()
	return answer

	
#print('result = ' +  str(solution(v1)))
#print('result = ' +  str(solution(v2)))
#print('result = ' +  str(solution(v3)))
print('result = ' +  str(solution(v3)))
