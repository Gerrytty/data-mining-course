import numpy as np
import math


def generate_training_sample():
    training_x = list(np.random.rand(200) * 360)
    training_y = list(map(lambda x: math.sin(x), training_x))

    return training_x, training_y


def f(x):
    return 1 / (1 + np.exp(-x))


def calc_node(inputs, weights):
    node_sum = 0

    for i in range(len(inputs)):
        node_sum += inputs[i] * weights[i]

    return f(node_sum)


# The derivative of the Sigmoid function.
# This is the gradient of the Sigmoid curve.
# It indicates how confident we are about the existing weight.
def sigmoid_derivative(x):
    return x * (1 - x)


if __name__ == "__main__":

    inputs = [1, 2]

    w = [
        [[0.1, 0.2], # выход на первый нейрон
         [0.15, 0.08]], # выход на второй нейрон
        [[0.1, 0.2],  # выход на первый нейрон
         [0.15, 0.08]],
        [[0.05, 0.2]]
    ]

    inputs_arr = inputs.copy()

    for i in range(len(w)):
        print(f"layer = {i}")
        print(f"inputs = {inputs_arr}")
        out_puts = []

        for j in w[i]:
            out_puts.append(calc_node(inputs_arr, j))

        print(f"ouputs = {out_puts}")

        inputs_arr = out_puts

    ans = inputs_arr[0]
    print(f"Answer is {inputs_arr[0]}")