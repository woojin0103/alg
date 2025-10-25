# def practice (arr,k):
#     arr_sorted = sorted(arr)
#     n = len(arr_sorted)
#     res = []
#
#     count = 1
#     for j in range(1,n):
#         if arr_sorted[j] == arr_sorted[j-1]:
#             count += 1
#         else:
#             if count >= k:
#                 res.append(arr_sorted[j-1])
#             count = 1
#     return res
#
# arr = [1,3,3,2,2,2,5,3,1,2]
# k=3
# ans = practice(arr,k)
# print(ans)

def practice (A,B):
    sorted_A = sorted(A)
    sorted_B = sorted(B)
    j,k = 0,0
    res = []

    while j < len(sorted_A) and k < len(sorted_B):
        if sorted_A[j] == sorted_B[k]:
            res.append(sorted_B[j])
            j += 1
            k += 1
        elif sorted_A[j] > sorted_B[k]:
            k += 1
        else:
            j += 1
    return res

A = [4,9,5,4,4]
B = [9,4,9,8,4]
print(practice(A,B))