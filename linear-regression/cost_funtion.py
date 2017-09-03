# evaluating and plotting cost function for univariate linear regression model
import matplotlib.pyplot as plt

# cost function for linear y = mx + c = 1/2m sum((y-x)^2)
# for this example the y-intercept = 0

def calculate_y_value(x, slope):
    y_values = [(slope * i) for i in x]
    return y_values


def calculate_cost_value(y_values, actual_output, m):
    total_squared_differnce = 0
    for i in range(m):
        difference = y_values[i] - actual_output[i]
        difference_squared = difference ** 2
        total_squared_differnce = total_squared_differnce + difference_squared

    return total_squared_differnce / (2 * m)


def slope_with_min_cost(cost_values, test_slopes):
    min_cost_value = min(cost_values)
    index_min_value = cost_values.index(min_cost_value)

    return test_slopes[index_min_value]


def main():
    x = [i for i in range(1, 4)]  # input values
    actual_output = [i for i in x]  # given output values
    m = len(x)  # value of m(number of training set)
    test_slopes = [i for i in range(-50, 51)]  # test slopes for getting the best slopes
    cost_values = []
    for slope in test_slopes:
        y_values_for_slope = calculate_y_value(x, slope)
        cost_value = calculate_cost_value(y_values_for_slope, actual_output, m)
        cost_values.append(cost_value)

    min_slope_value = slope_with_min_cost(cost_values, test_slopes)
    print("Slope with minimum cost value : ", min_slope_value)

    plot_cost_values(cost_values, test_slopes)


def plot_cost_values(cost_values, test_slopes):
    # plot the graph of cost values against the slope values
    plt.plot(test_slopes, cost_values)
    plt.xticks(range(test_slopes[0], test_slopes[-1], 1))
    plt.show()


if __name__ == '__main__':
    main()
