
import numpy as np

# Input training data
n = int(input("Enter number of training samples: "))
features = int(input("Enter number of input features: "))

X = []
y = []

for i in range(n):
    print("\nTraining sample", i + 1)

    row = []
    for j in range(features):
        value = float(input("Enter feature " + str(j + 1) + ": "))
        row.append(value)

    target = int(input("Enter target (0 or 1): "))

    X.append(row)
    y.append(target)

X = np.array(X)
y = np.array(y)

weights = np.zeros(features)
bias = 0
learning_rate = float(input("Enter learning rate: "))
epochs = int(input("Enter number of epochs: "))

# Training
for epoch in range(epochs):
    for i in range(n):
        net = np.dot(X[i], weights) + bias
        prediction = 1 if net >= 0 else 0

        error = y[i] - prediction

        weights = weights + learning_rate * error * X[i]
        bias = bias + learning_rate * error

print("\nFinal Weights:", weights)
print("Final Bias:", bias)

# Test a new input
print("\nEnter test data:")
test = []

for j in range(features):
    value = float(input("Enter feature " + str(j + 1) + ": "))
    test.append(value)

net = np.dot(test, weights) + bias
prediction = 1 if net >= 0 else 0

print("Net Input:", net)
print("Predicted Class:", prediction)
