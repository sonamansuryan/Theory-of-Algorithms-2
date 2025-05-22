def jump_with_path(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    path = [0]

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest
            path.append(current_end)

            if current_end >= len(nums) - 1:
                break

    return jumps, path

nums = list(map(int, input("Ներմուծեք զանգվածը (օր.՝ 2,3,1,1,4): ").split(',')))

min_jumps, jump_path = jump_with_path(nums)
print("Նվազագույն ցատկերի քանակը:", min_jumps)
print("Քայլերի հաջորդականությունը (ինդեքսներ):", jump_path)
print("Քայլերի հաջորդականությունը (արժեքներ):", [nums[i] for i in jump_path])
