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
    real_answer = 0.5

    weights = [
        # выход с первого слоя на второй
        [[0.1, 0.2],     # выход на первый нейрон
         [0.15, 0.08]],  # выход на второй нейрон
        # выход со второго слоя на третий
        [[0.1, 0.2],     # выход на первый нейрон
         [0.15, 0.08]],  # выход на первый нейрон
        # выход на выходное значение
        [[0.05, 0.2]]    # выход на выход
    ]

    inputs_arr = inputs.copy()

    for iters in range(200):

        outs = []

        # forward
        print("Forward")
        for i, weights_on_layer in enumerate(weights):
            print(f"layer = {i}")
            print(f"inputs = {inputs_arr}")
            out_puts = []

            for connect_weights in weights_on_layer:
                out_puts.append(calc_node(inputs_arr, connect_weights))

            print(f"outputs = {out_puts}")
            outs.append(out_puts)

            inputs_arr = out_puts

        ans = inputs_arr[0]
        print(f"Answer is {inputs_arr[0]}")

        # back
        print("Back")

        # хранит weights deltas каждого нейрона предыдущего слоя
        weights_delta_arr = []
        for i, out in enumerate(outs[::-1]):
            print(f"{i} iter")
            if i == 0:
                for output_neuron in out:
                    # считаем ошибку на выходном нейроне
                    error = math.sqrt((real_answer - output_neuron) ** 2)
                    weights_delta = error * sigmoid_derivative(output_neuron)
                    weights_delta_arr.append(weights_delta)

                    # проход по входным синапсам выходного нейрона
                    synaptic_weights_arr = weights[len(weights) - (i + 1)]
                    print(synaptic_weights_arr)
                    for output_neuron_index, synaptic_weights in enumerate(synaptic_weights_arr):
                        for j, syn_w in enumerate(synaptic_weights):
                            new_w = get_changed_weight(syn_w, weights_delta, output_neuron)
                            weights[len(weights) - (i + 1)][output_neuron_index][j] = new_w
            else:
                errors = []

                # новый массив для хранения weights delta
                new_weights_delta_arr = []

                for output_neuron_index, output_neuron in enumerate(out):
                    print(f"out neuron = {output_neuron}")
                    for wd in weights_delta_arr:
                        print(f"weights delta {wd}")
                        layer_arr = weights[len(weights) - (i + 1)]
                        for neuron_index, neuron in enumerate(layer_arr):
                            for syn_index, syn_w in enumerate(neuron):
                                error = wd * syn_w
                                weights_delta = error * sigmoid_derivative(output_neuron)
                                new_w = get_changed_weight(syn_w, weights_delta, output_neuron)
                                weights[len(weights) - (i + 1)][output_neuron_index][syn_index] = new_w
                                new_weights_delta_arr.append(weights_delta)

                weights_delta_arr = new_weights_delta_arr
                print(weights_delta_arr)
