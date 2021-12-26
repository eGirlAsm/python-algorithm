#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
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
#	['h', 'face'],
#	['i', 'face'],
#	['j', 'jiba'],
#	['k', 'headgear'],
	]
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

	['zb', 'headgearsdsd'],

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


def final_process(bucket):
	pass

def figure_count(length):
	return 2 ** length - 1





def updown_match(up,down):
	print('matcing.....',up,'=>',down)
	result = 0
	for x in range(0,len(up)):
		f_r = figure_count(len(down) - (x+1))
		f_c = len(list(combinations(up, x+1)))
		result += f_r * f_c
	return result




def recursive(fixed_bucket):
	result = 0
	fixed_len = len(fixed_bucket)
	for index in range(0, fixed_len):
		if fixed_bucket[fixed_len-1] != fixed_bucket[index]:
#			print ('>>>>>> should match',fixed_bucket[fixed_len-1], ' => ',fixed_bucket[index], '======>>> index',index,fixed_len)
			result += updown_match(fixed_bucket,index)
				
	print('-------,result',result)
	return result

combined_bucket = []

def solution(clothes):
	answer = 0
	clothes = sorted(clothes)
	print ('data len = ', len(clothes))
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
		print ('^^^^^^^^ append to bucket', bucket)
		
#		for b in range(0,len(bucket)):
#			b_data = list(combinations(bucket, b+1))
#			b_len = len(b_data)
#			for bb in b_data:
#				print(list(bb))
#			print('b_len',b_len,b+1)
#		combined_bucket.append(combined_bucket)

		this_matched = figure_count(len(bucket))
		print ('this matched', this_matched,'len=',len(bucket))
		
		fixed_bucket.append(bucket.copy())
		fixed_case_len = len(fixed_bucket)

#        print('fixed len',fixed_case_len)

#		if fixed_case_len > 1:
#			result =  recursive( fixed_bucket)
##			print('result recursive',result)
#			this_matched += result

		total_matched += this_matched
		bucket.clear()
		
		
	print ('--------- total had matched = ', total_matched)
	row_count = len(fixed_bucket)
	outer_can_match_count = figure_count(row_count)
	print('row count', row_count)
	print('outer count',outer_can_match_count)
	print('remained match possible',outer_can_match_count - row_count)
	
	x = 0 
	while x < row_count:
		
#	g = []
#	for x in range(0,len(fixed_bucket)):
#		t = []
#		y = x + 1
#		t.append(fixed_bucket[x])
#		while y < len(fixed_bucket):	
#			t.append(fixed_bucket[y])
#			z = y + 1
#			while z < len(fixed_bucket):
#				t.append(fixed_bucket[z])
#				
#				z = z + 1
#			y = y + 1
#		tt = t.copy()
#		g.append(tt)
#	for gg in g:
#		print(gg)
#	r_bucket = []
#	temp_bucket  = []
#	index = 0
#	while row_count:
#		row_count -= 1
#		index = row_count
#		print(row_count)
#		temp_bucket.append(fixed_bucket[row_count])
#		while index >= 0:
#			if fixed_bucket[index] not in temp_bucket:
#				temp_bucket.append(fixed_bucket[index])
#			
#			index -= 1
#			print('index',index)
#
#		print('len temp',len(temp_bucket))
#		copy_bucket = temp_bucket.copy()
#		if len(copy_bucket) > 1 and copy_bucket not in r_bucket:
#			r_bucket.append(copy_bucket)
#		temp_bucket.clear()
#	print('lll--------------ll',len(r_bucket))
		
##	print(r_bucket)
#	for x in r_bucket:
#		print(x)
#	row_count = len(fixed_bucket)
#	outer_can_match_count = figure_count(row_count)
#	print('row count', row_count)
#	print('outer count',outer_can_match_count)
#	print('excepted solo',outer_can_match_count - row_count)
#	for x in range(row_count,1,-1):
##		print(fixed_bucket[x-1])
#		row = fixed_bucket[x-1]
#		row_col_count = figure_count(len(row))
#		for y in range(x,0,-1):
#			next_row = fixed_bucket[y-1]
#			if row != next_row:
##				print(row,'=>',next_row)
#				result = updown_match(row, next_row)
#				total_matched += result
#				print('result ',result)
#				print('xxxxx',x, 'yyyy',y)
#				z = y -1
#				while z and result:
#					
#					print('gogogogogogogogogogogogogogo ahead?',fixed_bucket[x-1],fixed_bucket[y-1], fixed_bucket[z-1])
#					x1_len = len(fixed_bucket[x-1])
##					print('x1_len',x1_len)
#					y1_len = len(fixed_bucket[y-1])
#					z1_count = y1_len - x1_len
#					z1_len = len(fixed_bucket[z-1])
#					
#					print('z1_len',z1_len,'real count',z1_len - z1_count,'gigure',figure_count(z1_len - z1_count))
#					
#					for k in range(1,y1_len):
#						print('kkk',k+1)
#						f_r = figure_count(z1_len - (k+1))
#						f_c = len(list(combinations(fixed_bucket[y-1], k+1)))
#						result += f_r * f_c
#					z -= 1
				
	return total_matched
	

#   print('result = ' +  str(solution(v1)))
#   print('result = ' +  str(solution(v2)))
#   print('result = ' +  str(solution(v3)))
#   print('result = ' +  str(solution(v4)))

print('total matched = ' + str(solution(v4)))
