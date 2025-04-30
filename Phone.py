Phone = input("Phone: ")
digits_mapping = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four"
}

output = ""

for ch in Phone:
    output += digits_mapping.get(ch, "!") + " " 
print(output)