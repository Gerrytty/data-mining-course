import matplotlib.pyplot as plt


def f(x):
    return x * x


def df(x):
    return 2 * x


# градиентный спуск
# находим точку минимума функции x^2
def gradient_descent():
    init_x = -20
    for i in range(1000):
        init_x -= df(init_x) * 0.1

    print(init_x)

    return init_x


if __name__ == "__main__":
    min_of_f = gradient_descent()
    y_of_min = f(min_of_f)

    x = [-i for i in range(0, 10)] + [i for i in range(0, 10)]
    y = [i * i for i in range(0, 10)] * 2

    plt.plot(x, y)
    plt.scatter(min_of_f, y_of_min)
    plt.show()
