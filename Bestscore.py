def first_sceond(my_list):
    
    max1, max2 = 0, 0
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
        
    return max1, max2

my_list = [95, 92, 98, 97, 85, 80, 92, 95, 96] 
print(first_sceond(my_list))