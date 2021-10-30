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

    total_num_of_values = len(X)

    max_x = np.max(X) + 1
    min_x = np.min(X) - 1

    # Calculating line values x and y
    x = np.linspace(min_x, max_x, total_num_of_values)


    for i in range(1, 5):
        # get the polynomial coefficients
        mymodel = np.poly1d(np.polyfit(X, Y, i))

        myline = np.linspace(min_x, max_x, total_num_of_values)

        y_est = np.polyfit(X, Y, i)
        y_test = np.polyval(y_est, X)
        plt.subplot(2,2,i)

        plt.scatter(X, Y)
        plt.plot(myline, mymodel(myline),color='red')
        plt.title(f'Polynomial Degree {i}')

        # Calculating Root Mean Squares Error
        square_error = 0
        for i in range(total_num_of_values):
            square_error += (Y[i] - y_test[i]) ** 2
        square_error = np.sqrt(square_error / total_num_of_values)
        print("Square Error")
        print(square_error)
        #var = np.var(y_test)
        #print(f'var:  {var}')

    plt.show()

if __name__ == '__main__':
    regressionLine('linear.csv')
    regressionLine('outlier.csv')
    regressionLine('second_order.csv')
    regressionLine('third_order.csv')