def max_profit_with_steps(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(1, len(prices)):
        print(f"Օր {i + 1} | Գին: {prices[i]}")

        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
            print(f"Նոր նվազագույն գին՝ {min_price} (գնման օրը թարմացվում է)")
        else:
            profit = prices[i] - min_price
            print(f"Հաշվարկվող շահույթ՝ {prices[i]} - {min_price} = {profit}")
            if profit > max_profit:
                max_profit = profit
                sell_day = i
                print(f"Նոր առավելագույն շահույթ՝ {max_profit} (վաճառքի օրը թարմացվում է)")

    print("\nԳնելու լավագույն օրը՝", buy_day + 1)
    print("Վաճառքի լավագույն օրը՝", sell_day + 1)
    print("Առավելագույն շահույթ՝", max_profit)

    return max_profit


input_str = input("Մուտքագրեք բաժնետոմսերի գները (օր.՝ 7,1,5,3,6,4): ")
prices = list(map(int, input_str.strip().split(',')))

max_profit_with_steps(prices)
