
import numpy as np

class McCullochPittsNeuron:
    def __init__(self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold

    def activate(self, inputs):
        net = np.dot(inputs, self.weights)
        return 1 if net >= self.threshold else 0

w1 = float(input("Enter weight w1: "))
w2 = float(input("Enter weight w2: "))
threshold = float(input("Enter threshold: "))

neuron = McCullochPittsNeuron([w1, w2], threshold)

a = int(input("Enter input A (0 or 1): "))
b = int(input("Enter input B (0 or 1): "))

output = neuron.activate([a, b])

print("A AND NOT B =", output)
