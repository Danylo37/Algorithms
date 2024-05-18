from Practice2.generator import Generator
from Practice6.find import Find
import timeit


gen = Generator()
employees_10k = gen.generate_10_000()

f = Find()

for e in employees_10k:
    f.append(e)

employees_10k.sort()

print("list.index:")
time = timeit.timeit("employees_10k.index(employees_10k[0])", globals=globals(), number=100)
print(f"0th element: {time:.7f} seconds")
time = timeit.timeit("employees_10k.index(employees_10k[4998])", globals=globals(), number=100)
print(f"4998th element: {time:.7f} seconds")
time = timeit.timeit("employees_10k.index(employees_10k[9998])", globals=globals(), number=100)
print(f"9998th element: {time:.7f} seconds")

print()

print("f.find:")
time = timeit.timeit("f.find(employees_10k[0])", globals=globals(), number=100)
print(f"0th element: {time:.7f} seconds")
time = timeit.timeit("f.find(employees_10k[4998])", globals=globals(), number=100)
print(f"4998th element: {time:.7f} seconds")
time = timeit.timeit("f.find(employees_10k[9998])", globals=globals(), number=100)
print(f"9998th element: {time:.7f} seconds")

print()

print("f.exponential_search:")
time = timeit.timeit("f.exponential_search(employees_10k[0])", globals=globals(), number=100)
print(f"0th element: {time:.7f} seconds")
time = timeit.timeit("f.exponential_search(employees_10k[4998])", globals=globals(), number=100)
print(f"4998th element: {time:.7f} seconds")
time = timeit.timeit("f.exponential_search(employees_10k[9998])", globals=globals(), number=100)
print(f"9998th element: {time:.7f} seconds")
