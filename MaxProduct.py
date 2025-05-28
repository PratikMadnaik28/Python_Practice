def max_product(arr):
    max1, max2 = 0, 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2

arr = [1, 5, 10, 20, 7, 4]
print(max_product(arr))

    