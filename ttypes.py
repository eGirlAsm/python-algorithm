def replace(all_matched, clothes, bucket, baseIndex):
    for x in range(baseIndex + 1, len(clothes)):
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

    all_matched.clear()
    return answer


def solution1(clothes):
    bucket = []
    all_matched = []
    answer = 0
    clothes = sorted(clothes)
    print('ALL___ :: ',clothes)
    for x in range(0, len(clothes)):
        # typeList = [item[1] for item in bucket if len(bucket)]
        # print('types ', clothes[x][1])
        # print('typeList', typeList)
        if clothes[x][1] not in [item[1] for item in bucket if len(bucket)]:
            bucket.append(clothes[x])
    #		if clothes[x][1] not in typeList:
    #			bucket.append(clothes[x])

    # print('algorithm :: ',len(bucket) ** 2+1)
    x_base = 2* (2 ** (len(bucket) - 1) ) - 1
    print('x_base :: ', x_base)
    print('BUCKET :: ', bucket)
    answer = len(all_matched)

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

print(" result ", solution1(v3))