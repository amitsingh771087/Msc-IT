
# Fuzzy Set Operations

n = int(input("Enter number of elements: "))

A = {}
B = {}

for i in range(n):
    key = "x" + str(i + 1)
    A[key] = float(input("Enter membership of A for " + key + ": "))
    B[key] = float(input("Enter membership of B for " + key + ": "))

def fuzzy_union(A, B):
    return {x: max(A[x], B[x]) for x in A}

def fuzzy_intersection(A, B):
    return {x: min(A[x], B[x]) for x in A}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

def algebraic_sum(A, B):
    return {x: A[x] + B[x] - A[x] * B[x] for x in A}

def algebraic_product(A, B):
    return {x: A[x] * B[x] for x in A}

def bounded_sum(A, B):
    return {x: min(1, A[x] + B[x]) for x in A}

def bounded_difference(A, B):
    return {x: max(0, A[x] - B[x]) for x in A}

def probabilistic_or(A, B):
    return {x: A[x] + B[x] - A[x] * B[x] for x in A}

print("\nA =", A)
print("B =", B)

print("\n1. Union:", fuzzy_union(A, B))
print("2. Intersection:", fuzzy_intersection(A, B))
print("3. Complement of A:", fuzzy_complement(A))
print("4. Algebraic Sum:", algebraic_sum(A, B))
print("5. Algebraic Product:", algebraic_product(A, B))
print("6. Bounded Sum:", bounded_sum(A, B))
print("7. Bounded Difference:", bounded_difference(A, B))
print("8. Probabilistic OR:", probabilistic_or(A, B))
