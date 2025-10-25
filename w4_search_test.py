from w3_search import binary_search
from w3_search import linear_search
import time

sizes = [10_000_000,20_000_000,40_000_000,80_000_000]

print(f"{'n':>10} | {'선형탐색 시간(s)':>15} | {'이진탐색(s)':>15} | {'이론배수(n)':>10} |"
      f"{'실제배구(선형)':>10} | {'실제배수(이진)':>10}")

prev_linear = None
prev_binary = None

for idx, n in enumerate(sizes):
      nlist = list(range(n))
      target = n-1

      #선형 탐색 소요 시간
      # O(n)
      s = time.time()
      linear_search(nlist,target)
      e = time.time()
      linear_time = e-s

      #이진 탐색 소요 시간
      # O(log n)
      s = time.time()
      binary_search(nlist,target)
      e = time.time()
      binary_time = e-s

      if idx == 0:
            print(f"{n:10} | {linear_time:15.4f} | {binary_time:15.6f} | {'-':>10} | {'-':>10} | {'-':>10}")
      else:
            theory_linear = sizes[idx] / sizes[idx-1]
            real_linear = linear_time / prev_linear if prev_linear else 0
            real_binary = binary_time / prev_binary if prev_binary else 0
            print(f"{n:10} | {linear_time:15.4f} | {binary_time:15.6f} | {theory_linear:>10} | {real_linear:>10} | {real_binary:>10}")

      prev_linear = linear_time
      prev_binary = binary_time
