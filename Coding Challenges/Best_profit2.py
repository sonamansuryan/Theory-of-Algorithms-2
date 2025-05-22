def maxProfit(prices):
    profit = 0
    transactions = []

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            buy_day = i - 1
            sell_day = i
            buy_price = prices[buy_day]
            sell_price = prices[sell_day]
            profit += sell_price - buy_price
            transactions.append(
                f"Օր {buy_day+1}-ին գնիր {buy_price}-ով, Օր {sell_day+1}-ին վաճառիր {sell_price}-ով → շահույթ = {sell_price - buy_price}"
            )

    print("Քայլերի հաջորդականությունը շահույթով վաճառքի համար՝")
    for t in transactions:
        print(t)

    print(f"\nԸնդհանուր առավելագույն շահույթը՝ {profit}")
    return profit

prices_input = input("Ներմուծեք գների ցանկը, բաժանված ստորակետերով (օր.՝ 7,1,5,3,6,4): ")
prices = list(map(int, prices_input.strip().split(',')))

maxProfit(prices)
