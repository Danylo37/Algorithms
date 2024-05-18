from Practice2.generator import Generator
from Practice7.sort import Sort
import timeit


gen = Generator()
employees_1k = gen.generate_1000()

s = Sort(*employees_1k)

time = timeit.timeit("employees_1k.sort()", globals=globals(), number=100)
print(f"list.sort: {time:.7f} seconds")
time = timeit.timeit("employees_1k.sort(reverse=True)", globals=globals(), number=100)
print(f"list.sort reverse: {time:.7f} seconds")

print()

time = timeit.timeit("s.sort()", globals=globals(), number=100)
print(f"s.sort (mergesort): {time:.7f} seconds")
time = timeit.timeit("s.sort(reverse=True)", globals=globals(), number=100)
print(f"s.sort (mergesort) reverse: {time:.7f} seconds")
