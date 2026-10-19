
import numpy as np

X = []
Y = []

for i in range(4):
    print("\nPattern", i + 1)
    x1 = int(input("Enter x1 (-1 or 1): "))
    x2 = int(input("Enter x2 (-1 or 1): "))
    y = int(input("Enter target y (-1 or 1): "))

    X.append([x1, x2])
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

w = np.zeros(2)
b = 0

print("\nInitial Weights:", w)
print("Initial Bias:", b)

for i in range(len(X)):
    w = w + X[i] * Y[i]
    b = b + Y[i]

print("\nFinal Weights:", w)
print("Final Bias:", b)

print("\nTesting AND Function")
print("Input\tTarget\tOutput")

for i in range(len(X)):
    net = np.dot(X[i], w) + b
    output = 1 if net >= 0 else -1
    print(X[i], "\t", Y[i], "\t", output)
