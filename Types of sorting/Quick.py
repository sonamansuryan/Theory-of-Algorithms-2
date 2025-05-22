def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        print(f"Pivot ընտրված է: {pivot}")

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        print("Բաժանումից հետո:")
        print("Ընթացիկ ցուցակը:", arr)
        print("left:", left)
        print("middle:", middle)
        print("right:", right)

        return quick_sort(left) + middle + quick_sort(right)


list = list(map(int, input("Մուտքագրեք ցուցակի տարրերը՝ բաժանված բացատներով: ").split()))
sorted_list = quick_sort(list)
print("Սորտավորված ցուցակը: ", sorted_list)