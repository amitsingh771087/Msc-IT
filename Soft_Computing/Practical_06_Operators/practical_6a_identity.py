
# Identity Operators: is and is not

list1 = []
list2 = []
list3 = list1

n = int(input("Enter number of elements: "))

print("Enter elements for List 1:")
for i in range(n):
    list1.append(input())

print("Enter elements for List 2:")
for i in range(n):
    list2.append(input())

print("List 1:", list1)
print("List 2:", list2)

# Identity operators
print("list1 is list3:", list1 is list3)
print("list1 is list2:", list1 is list2)

print("list1 is not list2:", list1 is not list2)
print("list1 is not list3:", list1 is not list3)
