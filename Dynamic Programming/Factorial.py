def factorial_dp(n):
    # Ստեղծում ենք մի աղյուսակ, որում կպահենք արդյունքները
    dp = [1] * (n + 1)  # dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i

    return dp[n]

n = int(input("Մուտքագրեք n-ը ֆակտորիալի համար: "))
print(f"{n}! =", factorial_dp(n))
