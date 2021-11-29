from datetime import datetime
import random
import sorts

N = 200000

array = []
start = datetime.now().timestamp()
for i in range(N):
    array.append(random.randint(-N, N))
filled = datetime.now().timestamp() - start
print("Filled: " + str(filled))
start = datetime.now().timestamp()

# sorts.bubble_sort(array)
bubble = datetime.now().timestamp() - start

start = datetime.now().timestamp()

sorts.merge_sort(array)

merge = datetime.now().timestamp() - start

qar = array.copy()

start = datetime.now().timestamp()
sorts.quick_sort(qar, 0, N-1)
quick = datetime.now().timestamp() - start

start = datetime.now().timestamp()
array.sort()
py = datetime.now().timestamp() - start
print(f"Bubble sort: {bubble}\nMerge sort: {merge}\nQuick sort: {quick}\nPython: {py}")