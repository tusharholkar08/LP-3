def fractional_knapsack():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    res = 0

    # Pair: [Weight, Value]
    for pair in sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True):
        if capacity <= 0:  # Capacity completed - Bag fully filled
            break
        if pair[0] > capacity:  # Current's weight with highest value/weight ratio
            res += int(capacity * (pair[1]/pair[0]))  # Completely fill the bag
            capacity = 0
        else:  # Take the whole object
            res += pair[1]
            capacity -= pair[0]

    print(res)

fractional_knapsack()
