def bubbleSort(array):
    
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print("Lista ordenada:", array)

array = [5, 10, 14, 18, 20, 13, 27, 29,  19, 15, 37, 3, 72, 81]

bubbleSort(array)
