
v1 = [["yellow_hat", "headgear"], ["blue_sunglasses",
								   "eyewear"], ["green_turban", "headgear"]]
v2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
v3 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"],
	  ["e", "headgear"], ["f", "leg"], ["g", "face"], ["h", "face"]]
v4 = [["a", "face"], ["b", "face"], ["c", "face"], ["d", "headgear"], ["e", "headgear"], ["f", "headgear"], ["g", "headgear"], ["h", "headgeara"], ["i", "headgearb"], ["j", "headgearasdf"], ["k", "headgearc"], ["l", "headgeard"], ["m", "headgeare"], ["n", "headgearf"], ["o", "headgear"], [
	"p", "headgear"], ["q", "headgear"], ["r", "headgear"], ["s", "headgearfda"], ["t", "headgearsd"], ["u", "headgearfd"], ["v", "headgearasdf"], ["w", "headgearfdf"], ["x", "headgearaaa"], ["y", "headgear"], ["z", "headgear"], ["za", "headgear"], ["zb", "headgearsdsd"], ["zc", "headgear"]]

v5 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"], ["h", "father"], ["i", "eye"], ["j", "face"], ["k", "leg"], [
	"l", "headgear"], ["m", "head"], ["n", "flower"], ["o", "mother"], ["p", "father"], ["q", "ilove"], ["r", "jurk"], ["s", "jurk"], ["t", "lllove"], ["u", "memi"], ["v", "nnnoo"]]
v6 = [["a", "eye"], ["b", "leg"], ["c", "leg"], ["d", "eye"], ["e", "hand"], ["f", "leg"]]

def figure_count(length):
	return 2**length-1

def recursive(matching_bucket,fixed_bucket):
#	if x == 1:
#		return 1
#	else:
#	print('matching bb', matching_bucket,'fixed',fixed_bucket)
	for index in range(0,len(fixed_bucket)):
#		print('should match1',fixed_bucket[index])
		if matching_bucket != fixed_bucket[index]:
			print('should match2',fixed_bucket[index])
			count = figure_count(len(matching_bucket))
			for x in range(0,count):
				print('x,x_value',x,matching_bucket)
				
			
#		print('difffff', len(matching_bucket),len(fixed_bucket[index]))
#		diff_len = len(fixed_bucket[index]) - len(matching_bucket)
#		print('diff len',diff_len)
#		print('fixed',fixed_bucket[index])
#		print('index',index)

def solution(clothes):
	answer = 0
	clothes = sorted(clothes)
	print('data len = ', len(clothes))
	bucket = []
	total_matched = 0
	fixed_bucket = []
	excepted_bucket = clothes.copy()

	last_figure = 0
	last_length = 0
	while len(excepted_bucket):
		temp_bucket = excepted_bucket.copy()
		for x in excepted_bucket:
			type_list = [item[1] for item in bucket]
			if x[1] not in type_list:
				bucket.append(x)
				temp_bucket.remove(x)
		excepted_bucket = temp_bucket.copy()
		print('loaded bucket', bucket)
		
		this_matched = figure_count(len(bucket))
		print("this matched", this_matched)
		
		
		fixed_bucket.append(bucket.copy())
		fixed_case_len = len(fixed_bucket)
#		print('fixed len',fixed_case_len)
		
		
		if fixed_case_len > 1:
			recursive(fixed_bucket[fixed_case_len-1], fixed_bucket)
#		recursive(fixed_bucket)
#		for index in range(0,len(fixed_bucket)):
#			print('figure >>>> ',(figure_count(len(fixed_bucket[index])) - figure_count(len(bucket)) - 1) * len(bucket))
#			print('item every need match >>>>>  ',fixed_bucket[index],figure_count(this_matched))
#			total_matched += figure_count(this_matched)
#			for match_rotate in range(1,this_matched):
#				print('rotate',match_rotate)
#				print('fifififi ',len(bucket) / match_rotate)
#				print('asdjflasdj',len(fixed_bucket[index]),len(fixed_bucket[match_rotate] ))
				# 13 - 
#				r = figure_count(len(fixed_bucket[index]) - match_rotate) * int(len(bucket) / match_rotate)
#				print('llfaaa',r)
#				total_matched += r
				
		

		total_matched += this_matched
		bucket.clear()

	print('--------- total had matched = ', total_matched)
	return answer

#   print('result = ' +  str(solution(v1)))
#   print('result = ' +  str(solution(v2)))
#   print('result = ' +  str(solution(v3)))
#   print('result = ' +  str(solution(v4)))
print('result = ' + str(solution(v6)))
