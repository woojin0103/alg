def linear_search(arr, target):
    for j,v in enumerate(arr):
        if v == target:
            return j
    return -1
# 그냥 하나씩 찾기
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1
# arr을 sorted함수로 정렬한다음 중간,중간의 왼쪽, 중간의 오른쪽으로 비교해서 찾기

arr = [8,3,7,2,9,4]
target = 7
sorted_arr = sorted(arr)
print("선형탐색")
print(linear_search(arr,target))

print("이진탐색")
print("sorted_arr:", sorted_arr)
print(binary_search(sorted_arr,target))