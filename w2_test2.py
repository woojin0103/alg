# 두 리스트에서 중복을 포함한 교집합 구하기
# 교집합 결과를 오름차순으로 정렬하기
# sorted 함수 사용 가능, set 연산 활용할 수 없음

def intersection_navie(A,B):
    res = []
    for j in A:
        for k in B:
            if j == k:
                res.append(k)
                B.remove(k)
                break
    res = sorted(res)
    return res

def intersection_efficient(A,B):
    a_sorted = sorted(A)
    b_sorted = sorted(B)
    j,k = 0,0
    res = []

    while j < len(a_sorted) and k < len(b_sorted):
        if a_sorted[j] == b_sorted[k]:
            res.append(a_sorted[j])
            j += 1
            k += 1
        elif a_sorted[j] < b_sorted[k]:
            j += 1
        else:
            k += 1
    return res

A = [4,9,5,4,4]
B = [9,4,9,8,4]

#print(intersection_navie(A,B)) 
print(intersection_efficient(A,B))