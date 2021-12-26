
v1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
v2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
v3 = [["a", "eye"],  ["e", "face1"], ["f", "face2"], ["g", "face3"]]

v4 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"],
      ["e", "headgear"], ["f", "leg"], ["g", "face"], ["h", "face"]]

def add(all_matched, clothes, bucket, baseIndex):
	copy = bucket.copy()
	for x in range(baseIndex+1,len(clothes)):
		if clothes[x][1] not in [item[1] for item in copy]:
			copy.append(clothes[x])
		replace(all_matched, clothes, copy,x)
	copy.clear()
	
def replace(all_matched, clothes, bucket, baseIndex):
	for x in range(baseIndex+1,len(clothes)):
		copy = bucket.copy()
		if clothes[x][1] not in [item[1] for item in copy]:
			copy.append(clothes[x])
			clothes_names =  [item[0] for item in copy]
			if clothes_names not in all_matched:
				all_matched.append(clothes_names )
				replace(all_matched, clothes, copy, x)
	
		copy.clear()
		

def solution(clothes):
	bucket = []
	all_matched = []
	answer = 0

	clothes = sorted(clothes)
	for x in range(0,len(clothes)):
		bucket.append(clothes[x])
		all_matched.append( [item[0] for item in bucket] )
			
		replace(all_matched, clothes, bucket, x)
		
		add(all_matched, clothes, bucket, x)
		bucket.clear()
	
	answer = len(all_matched)
	for x in all_matched:
		print(' + '.join(x))
	all_matched.clear()
	return answer

	
#print('result = ' +  str(solution(v1)))
#print('result = ' +  str(solution(v2)))
print('result = ' +  str(solution(v4)))
