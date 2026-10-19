
import math

x = float(input("Enter the input x = "))
b = float(input("Enter the input b = "))
w = float(input("Enter the input w = "))

# Calculate net input
net = (x * w) + b
print("Net =", net)

# Binary sigmoidal function
binary_sigmoidal = 1 / (1 + math.exp(-net))

# Bipolar sigmoidal function
bipolar_sigmoidal = (
    (1 - math.exp(-net)) /
    (1 + math.exp(-net))
)

print("Binary Sigmoidal =", round(binary_sigmoidal, 2))
print("Bipolar Sigmoidal =", round(bipolar_sigmoidal, 4))
