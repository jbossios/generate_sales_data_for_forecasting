import numpy as np
from random import uniform
import matplotlib.pyplot as plt


def linear_function(x: float, slope: float = 150, intercept: float = 1000) -> float:
    return slope * x + intercept


def gen_point(x: float):
    # obtain y value
    y = linear_function(x)
    # return shifted y value
    return y + uniform(-100, 100)


def gen_data(make_plot = False):
    # generate the data
    x = np.array([x for x in range(100)]).reshape((-1, 1))
    y = np.array([gen_point(val) for val in x]).reshape((-1, 1))
    data = np.concatenate((x, y), axis=1)

    # save data to CSV file
    np.savetxt('data.csv', data, delimiter=',', header = 'days,sales')

    # plot data
    if make_plot:
        plt.scatter(x, y)
        plt.show()


if __name__ == '__main__':
    gen_data(make_plot = False)
