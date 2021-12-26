
v1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
v2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
v3 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "headgear"], ["f", "leg"], ["g", "face"], ["h", "face"]]
v4 = [["a", "face"], ["b", "face"], ["c", "face"], ["d", "headgear"], ["e", "headgear"], ["f", "headgear"], ["g", "headgear"], ["h", "headgeara"], ["i", "headgearb"], ["j", "headgearasdf"], ["k", "headgearc"], ["l", "headgeard"], ["m", "headgeare"], ["n", "headgearf"], ["o", "headgear"], ["p", "headgear"], ["q", "headgear"], ["r", "headgear"], ["s", "headgearfda"], ["t", "headgearsd"], ["u", "headgearfd"], ["v", "headgearasdf"], ["w", "headgearfdf"], ["x", "headgearaaa"], ["y", "headgear"], ["z", "headgear"], ["za", "headgear"], ["zb", "headgearsdsd"], ["zc", "headgear"]]


v5 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"], ["h", "father"],["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"], ["h", "father"], ["i", "ilove"],["j", "jurk"],["k", "jurk"],["l", "lllove"],["m", "memi"],["n", "nnnoo"]]

		
v6 = [["a", "eye"], ["b", "face"], ["c", "face"],["d", "face2"],["e","face3"],["f","face4"]]

def solution(clothes):
	
	
	answer = 0
	clothes = sorted(clothes)
	
	print('data len = ',len(clothes))
	
	overcount = 0
	
	bucket = []
	total_matched = 0
	
	excepted_bucket = clothes.copy()
	
	count_bucket = []
	while len(excepted_bucket):
#		print(len(excepted_bucket))
#		print(excepted_bucket)
#		print('empty bucket',bucket)
		temp_bucket = excepted_bucket.copy()
		for x in excepted_bucket:
#			print(x)
			type_list = [item[1] for item in bucket]
			if x[1] not in type_list:
				bucket.append(x)
				temp_bucket.remove(x)
		excepted_bucket = temp_bucket.copy()
	#					print(x)
		print('loaded bucket',bucket)
#		print('after remove',excepted_bucket)
		
		count_bucket.append(len(bucket))
		
		x_base = 2**(len(bucket) - 1)

		this_matched = x_base + x_base - 1
		print("this matched",this_matched)
		total_matched += this_matched
		
		
		bucket.clear()

#		overcount += 1
#		if overcount > 10000:
#			break
	print(count_bucket)
#	mul = 1
#	for x in count_bucket:
#		mul = mul * x
	
#	print('mul',mul)
	print('--------- total had matched = ',total_matched + 1 )
	return answer


#print('result = ' +  str(solution(v1)))
#print('result = ' +  str(solution(v2)))
#print('result = ' +  str(solution(v3)))
#print('result = ' +  str(solution(v4)))
print('result = ' +  str(solution(v6)))