# quick sort 알고리즘 작성하기 시험문제 출제
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    print(pivot,left,right)

    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [9,3,7,5,6,4,8,2]
print(quick_sort(arr))


#merge sort 알고리즘은 빈칸체우기 시험문제 출제
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge(left,right)
    result = []
    i=0
    j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    print(left,right,result)
    return result

arr = [12,11,13,5,6,7]
print(merge_sort(arr))