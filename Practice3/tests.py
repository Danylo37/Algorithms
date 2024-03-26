from Practice3.array import Array
from Practice2.generator import Generator


def print_array(arr):
    for j in arr:
        print(j)


generator = Generator()
employees = []

for i in range(5):
    employees.append(generator.generate_single())

array = Array(*employees)

print("Employees in array (iter): ")
print_array(array)

print()

print("Array length:")
print(len(array))

print()

print("Array repr:")
print(array)

print()

print("Array get item:")
print(array[0])
print(array[:2])

print()

print("Array set item:")
array[0] = array[1]
print_array(array)

print()

print("Array append:")
array.append(employees[2])
print_array(array)

print()

print("Array insert:")
array.insert(0, employees[3])
print_array(array)

print()

print("Array index:")
print(array.index(employees[1]))

print()

print("Array remove:")
array.remove(employees[1])
print_array(array)

print()

print("Array copy and clear:")
array_copy = array.copy()
print(array_copy)
print(id(array_copy[0]) == id(array[0]))
print(array)
array_copy.clear()
print(array_copy)

print()

print("Array del:")
del array[0]
print_array(array)

print()

print("Array extend:")
array.extend((employees[0], employees[1]))
print_array(array)

print()

print("Array pop:")
print(array.pop(0), "\n")
print_array(array)

print()

print("Array reverse:")
array.reverse()
print_array(array)

print()

print("Array count:")
print(array.count(employees[1]))
print(array.count(employees[2]))
print(array.count(employees[3]))

print()

print("Array deepcopy:")
array_deepcopy = array.deepcopy()
print(array)
print(array_deepcopy)
print(id(array_deepcopy[0]) != id(array[0]))

print()

print("Array min:")
print(array.min())

print()

print("Array max:")
print(array.max())

print()

print("Array add:")
print(array + array)

print()

print("Array mul:")
print(array * 2)
