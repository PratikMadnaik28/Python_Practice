numbers = [2, 5, 7, 7, 1, 1, 5, 2]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)