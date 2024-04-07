from Practice4.doublelinkedlist import DoubleLinkedList
from Practice2.generator import Generator


def print_dll(dll_):
    for j in dll_:
        print(j)


generator = Generator()
employees = []

for i in range(5):
    employees.append(generator.generate_single())

dll = DoubleLinkedList(*employees)

print("Employees in array (iter): ")
print_dll(dll)

print()

print("DoubleLinkedList length:")
print(len(dll))

print()

print("DoubleLinkedList repr:")
print(dll)

print()

print("DoubleLinkedList get item:")
print(dll[0])
print(dll[:2])

print()

print("DoubleLinkedList set item:")
dll[0] = dll[1]
print_dll(dll)

print()

print("DoubleLinkedList append:")
dll.append(employees[2])
print_dll(dll)

print()

print("DoubleLinkedList contains")
print(employees[3] in dll)
print(generator.generate_single() in dll)

print()

print("DoubleLinkedList insert:")
dll.insert(0, employees[3])
print_dll(dll)

print()

print("DoubleLinkedList index:")
print(dll.index(employees[1]))

print()

print("DoubleLinkedList remove:")
dll.remove(employees[1])
print_dll(dll)

print()

print("DoubleLinkedList copy and clear:")
dll_copy = dll.copy()
print(dll_copy)
print(id(dll_copy[0]) == id(dll[0]))
print(dll)
dll_copy.clear()
print(dll_copy)

print()

print("DoubleLinkedList del:")
del dll[0]
print_dll(dll)

print()

print("DoubleLinkedList extend:")
dll.extend((employees[0], employees[1]))
print_dll(dll)

print()

print("DoubleLinkedList pop:")
print(dll.pop(0), "\n")
print_dll(dll)

print()

print("DoubleLinkedList reverse:")
dll.reverse()
print_dll(dll)

print()

print("DoubleLinkedList count:")
print(dll.count(employees[1]))
print(dll.count(employees[2]))
print(dll.count(employees[3]))

print()

print("DoubleLinkedList deepcopy:")
dll_deepcopy = dll.deepcopy()
print(dll)
print(dll_deepcopy)
print(id(dll_deepcopy[0]) != id(dll[0]))

print()

print("DoubleLinkedList min:")
print(dll.min())

print()

print("DoubleLinkedList max:")
print(dll.max())

print()

print("DoubleLinkedList add:")
print(dll + dll)

print()

print("DoubleLinkedList mul:")
print(dll * 2)
