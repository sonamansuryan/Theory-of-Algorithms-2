def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Լրացնում ենք DP աղյուսակը
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    # Հետ ենք գնում պարզելու համար, որ իրերն են ընտրվել
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Այս իրը ընտրվել է
            selected_items.append(i - 1)  # Պահպանում ենք ինդեքսը
            w -= weights[i - 1]

    print("\nDP Աղյուսակ:")
    for row in dp:
        print(row)

    return dp[n][capacity], selected_items

n = int(input("Իրերի քանակը: "))
weights = list(map(int, input("Քաշերը (բացատով բաժանված): ").split()))
values = list(map(int, input("Արժեքները (բացատով բաժանված): ").split()))
capacity = int(input("Ուսապարկի տարողությունը: "))

# Հաշվում ենք
max_value, selected = knapsack(weights, values, capacity)

print("\nՄաքսիմալ արժեք:", max_value)
print("Ընտրված իրերի ինդեքսները (0-հիմքով):", selected)
for i in selected:
    print(f"   • Իրը #{i+1} — քաշ: {weights[i]}, արժեք: {values[i]}")
