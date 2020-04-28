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
    ['o', 'headgear'],
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


def updown_match(up, down):
    print('matcing.....', up, '=>', down)
    result = 0
    for x in range(0, len(up)):
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
            result += updown_match(fixed_bucket, index)

    print('-------,result', result)
    return result


def figure_matching_count(fixed_bucket, base_bucket, start_index):
    bucket = []
    # print('basasease',base_bucket,'startINdex',start_index)
    for x in range(start_index, len(fixed_bucket)):
        # print(fixed_bucket[x])
        temp = base_bucket.copy()
        if fixed_bucket[x] not in temp:
            temp.append(fixed_bucket[x])
            bucket.append(temp)
            

    return bucket

def calculate_three_more(bucket):
    return 0

def calculate_bucket_ex(bucket):
    # bucket.reverse()
    result = 0
    last_len = 0
    if len(bucket) >= 3:
        result = calculate_three_more(bucket)
    else:
        for x in range(0,len(bucket)):
            print("calc bucket ",bucket[x],x)
            if (x+1) < len(bucket):
                for y in range(0, len(bucket[x])):
                    f_r = figure_count(len(bucket[x-1]) - (y+1))
                    f_c = len(list(combinations(bucket[x],(y+1))))
                    print('frrrr',f_r,'fc',f_c)
                    result += f_r * f_c
        # print('eeeeeeee',bucket[x],len(bucket))
        # get count
        # if (x+1) < len(bucket):
        #     print('has next',x+1)
        #     # just get len and continue
        #     last_len = len(bucket[x]) - last_len
        # else:
            # remained_len = len(bucket[x]) - last_len
            # print("start calculate",remained_len,figure_count(remained_len))
            # result += remained_len
            # print("lllllast len",last_len,bucket[x-1])
            # start_index = 0
            # if len(bucket) >= 3:
            #     start_index = 1
            #     print("start index ccccccccchanged========",start_index)
            # for y in range(start_index, len(bucket[x-1])):
            #     print("yyyyyyy",y)
            #     f_r = figure_count(len(bucket[x]) - (y+1))
            #     f_c = len(list(combinations(bucket[x-1], y+1)))
            #     if start_index:
            #         f_c = len(bucket[x-1]) - y
            #     print('frrrr',f_r,'fc',f_c)
            #     result += f_r * f_c
            # print("no next figure out",result)
            # for y in range(0,len(bucket[x])):
            #     print('y',y)
                
            # while True:
                    
                # is final then return
                
            # f_r = 0
            # if (x+1) < len(bucket):
            #     for y in range(0, len(bucket[x])):
            #         if y > 1:
            #             f_r = figure_count(len(bucket[x+1]) - (y+1))
            #             f_c = len(list(combinations(bucket[x],(y+1))))
            #             print('frrrr',f_r,'fc',f_c)
            #             result += f_r * f_c
    print('eeeexxxx----------->',result)
    return result

def calculate_bucket(bucket):
    match_count = 0
    for x in range(0,len(bucket)):
        match_count += calculate_bucket_ex(bucket[x])   
    
    return match_count

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
        print('^^^^^^^^ append to bucket', bucket)

        this_matched = figure_count(len(bucket))
        print('this matched', this_matched, 'len=', len(bucket))

        fixed_bucket.append(bucket.copy())
        fixed_case_len = len(fixed_bucket)

#        print('fixed len',fixed_case_len)

#		if fixed_case_len > 1:
#			result =  recursive( fixed_bucket)
# print('result recursive',result)
#			this_matched += result

        total_matched += this_matched
        bucket.clear()
    print('--------- ---------------total had matched = ', total_matched)
    
    
    re_matched = 0
    
    row_count = len(fixed_bucket)
    outer_can_match_count = figure_count(row_count)
    print('row count', row_count)
    print('outer count', outer_can_match_count)
    print('excepted solo', outer_can_match_count - row_count)

    fixed_bucket.reverse()
    # print(fixed_bucket)
    row = 0
    col = 0
    bucket_index = 0
    
    my_bucket = []
    
    while row < row_count:

        col = row

        temp = []
        temp.append(fixed_bucket[row])

        my_bucket.append(temp) 
        print(temp)
        # print('fixxixix',fixed_bucket[row])
        while True:
            # figure out matched
            r = figure_matching_count(fixed_bucket,temp,row)
            # print(r)
            
            total_matched += calculate_bucket(r)

            my_bucket.append(r)
            if not len(r) or (len(r[0]) + row) >= row_count: break
            # print('lelelen',len(r[0]))

            col += 1
            temp.append(fixed_bucket[col])
            
        row += 1

    return total_matched


#   print('result = ' +  str(solution(v1)))
#   print('result = ' +  str(solution(v2)))
#   print('result = ' +  str(solution(v3)))
#   print('result = ' +  str(solution(v4)))

print('total matched = ' + str(solution(v4)))
