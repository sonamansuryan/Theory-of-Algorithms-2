def findTargetSumWays(nums, target):
    result = []

    def dfs(i, total, expression):
        if i == len(nums):
            if total == target:
                result.append(expression)
            return

        dfs(i + 1, total + nums[i], expression + ['+' + str(nums[i])])

        dfs(i + 1, total - nums[i], expression + ['-' + str(nums[i])])

    dfs(0, 0, [])

    print("Հնարավոր տարբերակների քանակը:", len(result))
    print("Տարբերակները, որոնց դեպքում ստացվում է", target, "՝")
    for expr in result:
        print(" ".join(expr))

nums_input = input("Ներմուծեք թվերի ցուցակը (օր.՝ 1,1,1,1,1): ")
target_input = int(input("Ներմուծեք թիրախային թիվը (target): "))

nums = list(map(int, nums_input.strip().split(',')))
target = target_input

findTargetSumWays(nums, target)
