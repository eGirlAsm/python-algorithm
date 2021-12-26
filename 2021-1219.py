test_cases = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
test_cases1 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]


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
        print("the clothes len" + str(len(clothes)))
        if len(clothes) <= 30:
            bucket.append(clothes[x])
            clothes_names = [item[0] for item in bucket]
            all_matched.append(clothes_names)
            replace(all_matched, clothes, bucket, x)
            bucket.clear()
    answer = len(all_matched)

    all_matched.clear()
    return answer


print(" the anwser is = " + str(solution(test_cases)))
print(" the anwser is = " + str(solution(test_cases1)))