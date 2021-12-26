#!/usr/bin/python4
# -*- coding: utf-8 -*-
from itertools import combinations
v1 = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'],
	  ['green_turban', 'headgear']]
v2 = [['crow_mask', 'face'], ['blue_sunglasses', 'face'],
	  ['smoky_makeup', 'face']]
v3 = [
	['a', 'eye'],
	['b', 'face'],
	['c', 'leg'],
	['d', 'headgear'],
	['e', 'headgear'],
	['f', 'leg'],
	['g', 'face'],
	['h', 'face'],
	]
v4 = [
	['a', 'face'],
	['b', 'face'],
	['c', 'face'],
	['d', 'headgear'],
	['e', 'headgear'],
	['f', 'headgear'],
	['g', 'headgear'],
	['h', 'headgeara'],
	['i', 'headgearb'],
	['j', 'headgearasdf'],
	['k', 'headgearc'],
	['l', 'headgeard'],
	['m', 'headgeare'],
	['n', 'headgearf'],
	['o', 'headgear'],
	['p', 'headgear'],
	['q', 'headgear'],
	['r', 'headgear'],
	['s', 'headgearfda'],
	['t', 'headgearsd'],
	['u', 'headgearfd'],
	['v', 'headgearasdf'],
	['w', 'headgearfdf'],
	['x', 'headgearaaa'],
	['y', 'headgear'],
	['z', 'headgear'],
	['za', 'headgear'],
	['zb', 'headgearsdsd'],
	['zc', 'headgear'],
	]
v5 = [["a", "eye"], ["b", "face"], ["c", "leg"], ["d", "headgear"], ["e", "head"], ["f", "flower"], ["g", "mother"], ["h", "father"], ["i", "eye"], ["j", "face"], ["k", "leg"], [
	"l", "headgear"], ["m", "head"], ["n", "flower"], ["o", "mother"]]
v6 = [
	['a', 'eye'],
	['b', 'leg'],
	['c', 'leg'],
	['d', 'eye'],
	['e', 'hand'],
	['f', 'leg'],
	]


def figure_count(length):
	return 2 ** length - 1

def recursive(matching_bucket, fixed_bucket):
	result = 0
	for index in range(0, len(fixed_bucket)):
		if matching_bucket != fixed_bucket[index]:
			count = len(matching_bucket)
			for x in range(0, count):
				f_r = figure_count(len(fixed_bucket[index]) - (x+1))
				f_c = len(list(combinations(matching_bucket, x+1)))
				result += f_r * f_c
	return result

def solution(clothes):
	clothes = sorted(clothes)
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
		this_matched = figure_count(len(bucket))
		fixed_bucket.append(bucket.copy())
		fixed_case_len = len(fixed_bucket)
		if fixed_case_len > 1:
			result =  recursive(fixed_bucket[fixed_case_len - 1], fixed_bucket)
			this_matched += result

		total_matched += this_matched
		bucket.clear()
	return total_matched


print('result = ' + str(solution(v4)))
