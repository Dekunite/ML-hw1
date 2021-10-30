import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

def regressionLine(filename):
    X = []
    Y = []

    my_data = genfromtxt(filename, delimiter=',')
    header_count = 0
    for data in my_data:
        if (header_count == 0):
            header_count = header_count + 1
        else:
            X.append(data[1])
            Y.append(data[2])

    x_mean = np.mean(X)
    y_mean = np.mean(Y)

    total_num_of_values = len(X)

    numerator = 0
    denominator = 0
    for i in range(total_num_of_values):
        numerator += (X[i] - x_mean) * (Y[i] - y_mean)
        denominator += (X[i] - x_mean) ** 2
        m = numerator / denominator
        constant = y_mean - (m * x_mean)

    max_x = np.max(X) + 1
    min_x = np.min(X) - 1

    # Calculating line values x and y
    x = np.linspace(min_x, max_x, total_num_of_values)
    y = constant + m * x

    # Ploting Line
    plt.plot(x, y, color='red', label='Regression Line')

    plt.scatter(X, Y)
    plt.title(filename)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    regressionLine('linear.csv')
    regressionLine('outlier.csv')
    regressionLine('second_order.csv')
    regressionLine('third_order.csv')