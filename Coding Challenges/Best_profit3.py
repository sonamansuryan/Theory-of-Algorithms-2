def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)
    dp = [[0] * n for _ in range(3)]  # dp[k][i]

    for k in range(1, 3):
        max_diff = -prices[0]
        print(f"\nՀաշվում ենք {k} գործարքի համար")
        for i in range(1, n):
            prev_profit = dp[k][i-1]
            possible_profit = prices[i] + max_diff
            dp[k][i] = max(prev_profit, possible_profit)
            max_diff = max(max_diff, dp[k-1][i] - prices[i])

            print(f"Օր {i + 1}: Գին = {prices[i]}")
            print(f"  Նախորդ շահույթ՝ dp[{k}][{i-1}] = {prev_profit}")
            print(f"  Գինը + max_diff = {prices[i]} + {max_diff - (dp[k-1][i] - prices[i])} = {possible_profit}")
            print(f"  Նոր շահույթ dp[{k}][{i}] = {dp[k][i]}")
            print(f"  Թարմացված max_diff = max({max_diff}, dp[{k-1}][{i}] - {prices[i]})")

    print("\nՎերջնական DP աղյուսակ՝")
    for k in range(3):
        print(f"{k} գործարք՝ {dp[k]}")

    return dp[2][n-1]

input_prices = input("Մուտքագրեք գների ցանկը (օրինակ՝ 3,3,5,0,0,3,1,4): ")
prices = list(map(int, input_prices.split(',')))
result = maxProfit(prices)
print("\nԱռավելագույն շահույթը՝", result)

