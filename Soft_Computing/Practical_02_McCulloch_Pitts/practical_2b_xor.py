
import numpy as np

class McCullochPittsNeuron:
    def __init__(self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold

    def activate(self, inputs):
        net = np.dot(inputs, self.weights)
        return 1 if net >= self.threshold else 0

a = int(input("Enter input A (0 or 1): "))
b = int(input("Enter input B (0 or 1): "))

or_neuron = McCullochPittsNeuron([1, 1], 1)
nand_neuron = McCullochPittsNeuron([-2, -2], -3)
and_neuron = McCullochPittsNeuron([1, 1], 2)

or_output = or_neuron.activate([a, b])
nand_output = nand_neuron.activate([a, b])

output = and_neuron.activate([or_output, nand_output])

print("OR Output =", or_output)
print("NAND Output =", nand_output)
print("XOR Output =", output)
