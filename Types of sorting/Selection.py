def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr

list = list(map(int, input("Մուտքագրեք ցուցակի տարրերը՝ բաժանված բացատներով: ").split()))
sorted_list= selection_sort(list)
print("Սորտավորված ցուցակը: ", sorted_list)