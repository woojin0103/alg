from w3_search import linear_search
from w3_search import binary_search

#linear_search와 binary_search 함수를 사용하여
# 다음과 같은 문제의 답을 구하시오

# card = [6,3,2,10,10]
# queries = [10,4,6]

# queries에 있는 모든 원소를 순회하면서, 해당 원소가 card에 있는지 탐색하는 알고리즘을
# linear_search와 binary_search 함수를 활용해 구현

card = [6,3,2,10,10]
queries = [10,4,6]

for q in queries:
    if linear_search(card,q) == -1:
        print(q, "NO")
    else:
        print(q, "YES")