def selection_sort(arr):
    n = len(arr)
    for i in range (n):
        min_index = i # assuming minimum element present at index 1
        for j in range (i + 1,n):
            if arr[j] < arr[min_index]: # finding actual minimum element
               min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]#swaping is done
            

arr = [7,4,5,2,1]
selection_sort(arr)
print(arr)

                