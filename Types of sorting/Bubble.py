def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


list = list(map(int, input("Մուտքագրեք ցուցակի տարրերը՝ բաժանված բացատներով: ").split()))
sorted_list = bubble_sort(list)
print("Սորտավորված ցուցակը: ", sorted_list)