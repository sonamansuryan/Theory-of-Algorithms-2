def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2


list_ = list(map(int, input("Մուտքագրեք ցուցակի տարրերը՝ բաժանված բացատներով: ").split()))
shell_sort(list_)
print("Սորտավորված ցուցակը: ", list_)