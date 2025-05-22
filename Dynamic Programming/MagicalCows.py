def magical_cows_queries(C: int, N: int, cows: list[int], queries: list[int]):
    max_day = max(queries)
    dp = [dict() for i in range(max_day + 2)]

    for cow_count in cows:
        dp[0][cow_count] = dp[0].get(cow_count, 0) + 1

    for day in range(max_day):
        for x in dp[day]:
            count = dp[day][x]
            if x <= C // 2:
                new_x = x * 2
                dp[day + 1][new_x] = dp[day + 1].get(new_x, 0) + count
            else:
                dp[day + 1][x] = dp[day + 1].get(x, 0) + count * 2

    for m in queries:
        total_farms = sum(dp[m].values())
        print(f"\n Օր {m}: {total_farms} ֆերմա")

C = int(input("Մուտքագրիր առավելագույն կովերի քանակը մեկ ֆերմայում (C): "))
N = int(input("Մուտքագրիր նախնական ֆերմաների քանակը (N): "))
cows = list(map(int, input(f"Մուտքագրիր {N} թվեր՝ կովերի քանակը յուրաքանչյուր ֆերմայում (օրինակ՝ 1 3 2 1): ").split()))
M = int(input("Մուտքագրիր հարցումների քանակը (M): "))
queries = list(map(int, input("Մուտքագրիր հարցումները՝ օրերի համար (օրինակ՝ 2 3 5): ").split()))

magical_cows_queries(C, N, cows, queries)
