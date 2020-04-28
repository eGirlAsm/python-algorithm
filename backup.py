def replace(all_matched, clothes, bucket, baseIndex):
	for x in range(baseIndex+1, len(clothes)):
		copy = bucket.copy()
		if clothes[x][1] not in [item[1] for item in copy]:
			copy.append(clothes[x])
			clothes_names = [item[0] for item in copy]
			if clothes_names not in all_matched:
				all_matched.append(clothes_names)
				replace(all_matched, clothes, copy, x)
		copy.clear()

def solution(clothes):
	bucket = []
	all_matched = []
	answer = 0
	clothes = sorted(clothes)
	for x in range(0, len(clothes)):
		bucket.append(clothes[x])
		clothes_names = [item[0] for item in bucket]
		all_matched.append(clothes_names)
		replace(all_matched, clothes, bucket, x)
		bucket.clear()
	answer = len(all_matched)
	
	
	for x in all_matched:
		print(' + '.join(x))
	
	all_matched.clear()
	return answer

v3 = [
	['a', 'eye'],
	['b', 'face'],
	['c', 'leg'],
	['d', 'headgear'],
	['e', 'headgear'],
	['f', 'leg'],
	['g', 'face'],
#	['h', 'face'],
#	['i', 'face'],
#	['j', 'jiba'],
#	['k', 'headgear'],
	]
v6 = [["a", "eye"], ["b", "leg"], ["c", "leg"], ["d", "eye"], ["e", "hand"], ["f", "leg"]]
v5 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"], ["h", "father"], ["i", "eye"], ["j", "face"], ["k", "leg"], [
	"l", "headgear"], ["m", "head"], ["n", "flower"], ["o", "mother"]]
v7 = [["a", "eye1"], ["b", "leg2"], ["c", "leg3"], ["d", "eye4"], ["e5", "hand6"], ["f", "leg7"]]
v4 = [
	['a', 'face'],
	['b', 'face'],
	['c', 'face'],
	['d', 'headgear'],
	['e', 'headgear'],


	['h', 'headgeara'],
	['i', 'headgearb'],
	['j', 'headgearasdf'],
	['k', 'headgearc'],
	['l', 'headgeard'],
	['m', 'headgeare'],
	['n', 'headgearf'],

	['s', 'headgearfda'],
	['t', 'headgearsd'],
	['u', 'headgearfd'],
	['v', 'headgearasdf'],
	['w', 'headgearfdf'],
	['x', 'headgearaaa'],

	['zb', 'headgearsdsd'],	]

print('result = ' + str(solution(v4)))
# 2^len(7) - 1