Phone = input("Phone: ")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
Output =""

for ch in Phone:
    Output += digits.get(ch, "!") + " "
print(Output)