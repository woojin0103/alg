import time
import numpy as np

print("O(n) 알고리즘 시간복잡도 확인 : 백터 덧셈")
n_list = [10_000_000, 20_000_000, 40_000_000, 80_000_000]
prev_time = None

for idx, n in enumerate(n_list):
    a = np.arange(n)
    b = np.arange(n)
    # np.arange(n)은 0부터 n-1까지의 정수 배열을 만듦
    # → a와 b는 각각 길이 n의 벡터

    start = time.time()
    c = a+b
    end = time.time()
    # 두 벡터를 원소별로 더함 → c[i] = a[i] + b[i]
    # 더하기 전의 시간을 측정하고 더한 후의 시간을 측정
    # 이 연산은 n개의 덧셈을 수행하므로 O(n)

    elapsed = end - start
    # elapsed에 걸린 시간을 저장
    if idx > 0:
        theory_ratio = n_list[idx] / n_list[idx-1]
        real_ratio = elapsed / prev_time
        print(f"n={n:10}, time={elapsed:.4f}초, 이론배수={theory_ratio:.1f}, 실제배수={real_ratio:.2f}")
    else:
        print(f"n={n:10}, time={elapsed:.4f}초, 첫 실험")
    prev_time = elapsed

print("0(n^2) 알고리즘 시간복잡도 확인 : 행렬 덧셈")
n_list = [1000,2000,4000,8000]
prev_time = None

for idx, n in enumerate(n_list):
    A = np.ones((n, n))
    B = np.ones((n, n))

    start = time.time()
    C = A+B
    end = time.time()

    elapsed  = end - start

    if idx > 0:
        theory_ratio = (n_list[idx] / n_list[idx-1]) ** 2
        real_ratio = elapsed / prev_time
        print(f"n={n:5}, time={elapsed:.4f}초, 이론배수={theory_ratio:.1f}배, 실제배수={real_ratio:.2f}배")
    else:
        print(f"n={n:5}, time={elapsed:.4f}, 첫 실험")

    prev_time = elapsed