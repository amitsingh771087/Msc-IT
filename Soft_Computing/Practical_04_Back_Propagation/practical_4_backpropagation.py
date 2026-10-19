
import math

w1 = float(input("Enter input-hidden weight: "))
b1 = float(input("Enter hidden bias: "))
w2 = float(input("Enter hidden-output weight: "))
b2 = float(input("Enter output bias: "))
lr = float(input("Enter learning rate: "))
x = float(input("Enter input value: "))
target = float(input("Enter target output: "))

# Forward propagation
net_h = w1 * x + b1
h = math.tanh(net_h)

net_o = w2 * h + b2
predicted = math.tanh(net_o)

error = target - predicted

# Backpropagation
sensitivity_o = -2 * (1 - predicted ** 2) * error
sensitivity_h = (
    (1 - h ** 2) * w2 * sensitivity_o
)

# Update weights
new_w2 = w2 + lr * sensitivity_o * h
new_w1 = w1 - lr * sensitivity_h

# Update biases
new_b2 = b2 + lr * sensitivity_o
new_b1 = b1 + lr * sensitivity_h

print("\nPredicted Output:", predicted)
print("Error:", error)
print("Updated Input-Hidden Weight:", new_w1)
print("Updated Hidden-Output Weight:", new_w2)
print("Updated Hidden Bias:", new_b1)
print("Updated Output Bias:", new_b2)
