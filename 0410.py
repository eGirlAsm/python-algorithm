
v1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
v2 = [["a", "face1"], ["b", "face2"], ["c", "face3"], ["d", "face4"], ["e", "face5"]]
v3 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"]]
v4 = [["a", "face"], ["b", "face"], ["c", "face"], ["d", "headgear"], ["e", "headgear"], ["f", "headgear"], ["g", "headgear"], ["h", "headgeara"], ["i", "headgearb"], ["j", "headgearasdf"], ["k", "headgearc"], ["l", "headgeard"], ["m", "headgeare"], ["n", "headgearf"], ["o", "headgear"], ["p", "headgear"], ["q", "headgear"], ["r", "headgear"], ["s", "headgearfda"], ["t", "headgearsd"], ["u", "headgearfd"], ["v", "headgearasdf"], ["w", "headgearfdf"], ["x", "headgearaaa"], ["y", "headgear"], ["z", "headgear"], ["za", "headgear"], ["zb", "headgearsdsd"], ["zc", "headgear"]]


v5 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"], ["h", "father"],["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"], ["h", "father"], ["i", "ilove"],["j", "jurk"],["k", "jurk"],["l", "lllove"],["m", "memi"],["n", "nnnoo"]]

v6 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "headgear"], ["f", "leg"], ["g", "face"], ["h", "face"]]
r_count = 0

def replace(all_matched, clothes, bucket, baseIndex):
	global r_count
#	print(f'r_count = {r_count}')
	r_count += 1
	for x in range(baseIndex+1,len(clothes)):
		copy = bucket.copy()
		if clothes[x][1] not in [item[1] for item in copy]:
			copy.append(clothes[x])
			clothes_names =  [item[0] for item in copy]
			if clothes_names not in all_matched:
				all_matched.append(clothes_names )
#		copy = []
				replace(all_matched, clothes, copy, x)
		
		copy.clear()
		

def solution(clothes):
	bucket = []
	all_matched = []
	answer = 0
	clothes = sorted(clothes)
	
	x_base = 2**(len(clothes) - 1)
	print("xbase",x_base,len(clothes))
	
	n_total_iterate = x_base + x_base - 1
	print('need iterate times = ',n_total_iterate )
	for i in range(0,n_total_iterate):
		print(i)
	
#	for x in range(0,len(clothes)):
#		bucket.append(clothes[x])
#		clothes_names = [item[0] for item in bucket]
#		all_matched.append( clothes_names)
#		replace(all_matched, clothes, bucket, x)
#		bucket.clear()
#	
#	answer = len(all_matched)
#	
#	
#	for x in all_matched:
#		print(' + '.join(x))
	
	# all_matched.clear()
	return answer


#print('result = ' +  str(solution(v1)))
#print('result = ' +  str(solution(v2)))
#print('result = ' +  str(solution(v3)))
#print('result = ' +  str(solution(v4)))
print('result = ' +  str(solution(v6)),len(v6))