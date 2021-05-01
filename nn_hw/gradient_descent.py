import matplotlib.pyplot as plt

learning_rate = 0.1


def f(x):
    return x * x


def df(x):
    return 2 * x


# градиентный спуск
# находим точку минимума функции x^2
def gradient_descent():
    minimum = -20
    for i in range(1000):
        minimum -= df(minimum) * learning_rate

    print(minimum)

    return minimum


if __name__ == "__main__":
    min_of_f = gradient_descent()
    y_of_min = f(min_of_f)

    x = [-i for i in range(0, 10)] + [i for i in range(0, 10)]
    y = [i * i for i in range(0, 10)] * 2

    plt.plot(x, y)
    plt.scatter(min_of_f, y_of_min)
    plt.show()
