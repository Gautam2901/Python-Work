def buy_chochlates(prices, money):
    # Sort the prices array
    prices.sort()

    left, right = 0, len(prices) - 1
    leftover = money

    while left < right:
        total_cost = prices[left] + prices[right]
        if total_cost <= money:
            leftover = money - total_cost
            left += 1
        else:
            right -= 1

    return leftover

prices1 = [1, 2, 2]
money1 = 3
print(buy_chochlates(prices1, money1))

prices2 = [3, 2, 3]
money2 = 3
print(buy_chochlates(prices2, money2))