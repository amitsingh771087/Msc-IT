# Soft Computing Practicals (1–8)

This folder contains Python programs for practicals 1 through 8. The notes below explain the main idea behind each practical, the inputs requested by its script, and how to run it.

## Requirements and running a program

- Python 3
- NumPy for practicals 2 and 3, and practical 8 (`pip install numpy`)
- The other scripts use only Python's standard library.

Run a script from the repository root with `python3 <path-to-script>`. For example:

```bash
python3 Soft_Computing/Practical_01_Simple_Neural_Network/practical_1a_snn.py
```

Enter each value when prompted. Use numeric values where requested; the programs are interactive and do not read an input file.

## Practical 1 — Simple neural network and sigmoid functions

### Theory

A single neuron forms its net input as `net = x × w + b`, where `x` is the input, `w` is its weight, and `b` is its bias. The activation function transforms this net value into the neuron output. The first program uses a clipped linear activation: values below 0 become 0, values from 0 to 1 are unchanged, and values above 1 become 1. The second program applies binary and bipolar sigmoid functions, which smoothly map a real-valued net input to `[0, 1]` and `[-1, 1]` respectively.

### Programs and inputs

| Program | Inputs |
| --- | --- |
| `Practical_01_Simple_Neural_Network/practical_1a_snn.py` | `x`, `b`, and `w` as numbers. Prints the net input and clipped output. |
| `Practical_01_Simple_Neural_Network/practical_1b_sigmoid.py` | `x`, `b`, and `w` as numbers. Prints the net input, binary sigmoid, and bipolar sigmoid. |

## Practical 2 — McCulloch–Pitts neurons and logic gates

### Theory

A McCulloch–Pitts neuron is a binary threshold unit. It calculates the weighted sum of binary inputs and outputs 1 when the sum is at least the threshold; otherwise, it outputs 0. The AND-NOT script lets you supply the weights and threshold. The XOR script combines threshold units to implement XOR, since XOR cannot be represented by one linear threshold unit alone.

### Programs and inputs

| Program | Inputs |
| --- | --- |
| `Practical_02_McCulloch_Pitts/practical_2a_andnot.py` | Weights `w1`, `w2`, a threshold, and inputs `A`, `B` (each 0 or 1). The chosen weights and threshold determine the gate behavior. |
| `Practical_02_McCulloch_Pitts/practical_2b_xor.py` | Inputs `A` and `B` (each 0 or 1). The script uses fixed OR, NAND, and AND neurons and prints their outputs and the XOR result. |

## Practical 3 — Hebbian learning rule

### Theory

Hebbian learning updates a connection weight using the product of an input and its target: `w = w + x × y`. The bias is accumulated from the targets. This program starts weights and bias at zero, applies the update once for each pattern, then uses a bipolar threshold (`net >= 0` gives 1, otherwise -1) to show the outputs. It is set up to demonstrate the bipolar AND function.

### Inputs

`Practical_03_Hebb_Rule/practical_3_and_hebb.py` asks for four patterns. For each pattern, enter `x1`, `x2`, and target `y`; each should be `-1` or `1`. Supply the four rows of the bipolar truth table and corresponding target values for the AND demonstration. NumPy is required.

## Practical 4 — Backpropagation in a small neural network

### Theory

The program has one input, one hidden neuron, and one output neuron, each using the hyperbolic tangent activation. It first propagates the input forward to calculate a prediction and error. It then calculates sensitivities using the derivative of `tanh`, and uses the learning rate to update the weights and biases for one training example.

### Inputs

`Practical_04_Back_Propagation/practical_4_backpropagation.py` asks for, in order: input-to-hidden weight, hidden bias, hidden-to-output weight, output bias, learning rate, input value, and target output. The `tanh` output range is `[-1, 1]`, so use a target in that range. The program performs one update and prints the prediction, error, and updated parameters.

## Practical 5 — Error backpropagation

### Theory

Error backpropagation measures the difference between a target and a network prediction, propagates the resulting gradient from the output neuron back to the hidden neuron, and adjusts weights and biases to reduce the error. This script uses the same one-input, one-hidden-neuron, one-output-neuron structure and `tanh` activation as practical 4. It performs one forward and backward pass for a single sample.

### Inputs

`Practical_05_Error_Back_Propagation/practical_5_error_backpropagation.py` asks for input-to-hidden weight, hidden bias, hidden-to-output weight, output bias, learning rate, input value, and target output. Use a target in `[-1, 1]` to match the `tanh` output. It prints the prediction, target, error, and updated parameters.

## Practical 6 — Python identity and membership operators

### Theory

Identity operators (`is` and `is not`) check whether two names refer to the same object in memory. They do not compare whether two separate lists contain equal values. Membership operators (`in` and `not in`) check whether a value occurs in a sequence or string.

### Programs and inputs

| Program | Inputs |
| --- | --- |
| `Practical_06_Operators/practical_6a_identity.py` | A count `n`, then `n` elements for List 1 and `n` elements for List 2. Elements are read as strings. The script also aliases List 1 as List 3 to demonstrate identity. |
| `Practical_06_Operators/practical_6b_membership.py` | Space-separated values for a list of numbers, a text string, a value to search for in the list, and a text fragment to search for in the string. All inputs are treated as strings. |

## Practical 7 — Fuzzy set operations

### Theory

In a fuzzy set, each element has a membership degree between 0 and 1 rather than only being present or absent. This program computes common operations element by element: union (maximum), intersection (minimum), complement (`1 − membership`), algebraic sum, algebraic product, bounded sum, and bounded difference. The program's probabilistic OR uses the same formula as its algebraic sum.

### Inputs

`Practical_07_Fuzzy_Set_Operations/practical_7_fuzzy_operations.py` first asks how many elements are in the universe. For each generated element (`x1`, `x2`, ...), enter its membership in set A and then in set B as decimal numbers from 0 to 1. It prints both sets and all calculated operations.

## Practical 8 — Perceptron classifier

### Theory

A perceptron is a linear binary classifier. It computes `net = dot(input, weights) + bias`, predicts class 1 when the net value is at least zero and class 0 otherwise, and updates its weights and bias by the learning rate times the classification error. Training is repeated over the supplied samples for the requested number of epochs.

### Inputs

`Practical_08_Perceptron/practical_8_perceptron.py` asks for the number of training samples and number of features. For each sample, enter one numeric value per feature followed by its target class (`0` or `1`). Then enter a learning rate and number of epochs. Finally, enter one feature value per feature for a test sample. The program prints the learned weights and bias, then the net input and predicted class for that test sample. NumPy is required.

## Input summary

- Practicals 1, 4, and 5 use numeric scalar values.
- Practical 2 uses binary inputs (`0` or `1`); practical 2a also accepts custom weights and threshold.
- Practical 3 uses bipolar values (`-1` or `1`) for four input/target patterns.
- Practical 6 reads strings, including values that may look numeric.
- Practical 7 requires membership degrees in `[0, 1]`.
- Practical 8 accepts numeric feature values and binary targets (`0` or `1`).
