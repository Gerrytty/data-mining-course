import numpy as np
import math


def generate_training_sample():
    training_x = list(np.random.rand(200) * 360)
    training_y = list(map(lambda x: math.sin(x), training_x))

    return training_x, training_y


# activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# The derivative of the Sigmoid function.
# This is the gradient of the Sigmoid curve.
# It indicates how confident we are about the existing weight.
def sigmoid_derivative(x):
    return x * (1 - x)


def get_changed_weight(input_weight, dw, out):
    print("get_changed_weight")
    print(f"input weight = {input_weight}")
    print(f"delta weight = {dw}")
    print(f"out = {out}")
    out_weight = input_weight * dw * out * 0.1
    print(f"new weight = {out_weight}")
    return out_weight


def calc_node(inputs, weights):
    node_sum = 0

    for i in range(len(inputs)):
        node_sum += inputs[i] * weights[i]

    return sigmoid(node_sum)


if __name__ == "__main__":

    inputs = [1, 2]
    real_answer = 4

    weights = [
        [[0.1, 0.2],     # выход на первый нейрон
         [0.15, 0.08]],  # выход на второй нейрон
        [[0.1, 0.2],     # выход на первый нейрон
         [0.15, 0.08]],
        [[0.05, 0.2]]
    ]

    inputs_arr = inputs.copy()

    outs = []

    # forward
    print("Forward")
    for i, weights_on_layer in enumerate(weights):
        print(f"layer = {i}")
        print(f"inputs = {inputs_arr}")
        out_puts = []

        for connect_weights in weights_on_layer:
            out_puts.append(calc_node(inputs_arr, connect_weights))

        print(f"ouputs = {out_puts}")
        outs.append(out_puts)

        inputs_arr = out_puts

    ans = inputs_arr[0]
    print(f"Answer is {inputs_arr[0]}")

    print(outs)

    # back
    print("Back")
    for i, out in enumerate(outs[::-1]):
        print(out)

        weights_delta = 0

        if i == 0:
            error = math.sqrt((real_answer - out[0]) ** 2)
            weights_delta = error * sigmoid_derivative(out[0])
            synaptic_weights = weights[len(weights) - 1]
            for j in range(len(synaptic_weights[0])):
                new_w = get_changed_weight(synaptic_weights[0][j], weights_delta, out[0])
                weights[len(weights) - 1][0][j] = new_w
        else:
            errors = []

            for neuron in out:
                # error = weights_delta * weights[len(weights) - (i + 1)]
                print(neuron)
                print(weights[len(weights) - (i + 1)])
            raise Exception