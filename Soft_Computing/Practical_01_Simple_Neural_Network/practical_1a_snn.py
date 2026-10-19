
# Simple Neural Network (SNN)

x = float(input("Enter the input x = "))
b = float(input("Enter the input b = "))
w = float(input("Enter the input w = "))

# Calculate net input
net = (x * w) + b
print("Net =", net)

# Activation function
if net < 0:
    out = 0
elif 0 <= net <= 1:
    out = net
else:
    out = 1

print("Output =", out)
