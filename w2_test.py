import time
import numpy as np
# 3번 이상 나온 수를 알려주는 함수 만들기
def frequency_at_least_k(arr,kk):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    res = []
    count = [0] * n
    for j in range(len(arr_sorted)):
        for k in range(len(arr_sorted)):
            if arr_sorted[j] == arr_sorted[k]:
                count[j] += 1

    for j in range(len(arr_sorted)):
        if count[j] >= kk:
            if arr_sorted[j] not in res:
                res.append(arr_sorted[j])

    ans=""
    if len(res) == 0: ans="None"
    else: ans=" ".join(str(x) for x in res)

    return ans

def frequency_at_least_k_ver2(arr,k):
    res = []
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    # sorted 함수는 python 내장함수고 인자로 리스트가 올력우 리스트의 원소를 오름차순으로 정렬한다

    count = 1
    for j in range(1,n):
        print(j)
        if arr_sorted[j] == arr_sorted[j-1]:
            count += 1
        else:
            if count >= k:
                res.append(arr_sorted[j-1])
                print(f"원소 {arr_sorted[j-1]}이 {count}번 등장하여 결과에 넣습니다.")
            count = 1

    ans = ""
    if len(res) == 0:
        ans = "None"
    else:
        ans = " ".join(str(x) for x in res)

    return ans


arr = [1,3,3,2,2,2,5,3,1,2]
k=3
ans = frequency_at_least_k(arr,k)
print(ans)

ans = frequency_at_least_k_ver2(arr,k)