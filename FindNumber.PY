myArray = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

def findnumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)

findnumber(myArray, 10)

