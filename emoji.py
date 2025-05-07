Message = input("> ")
Words = Message.split(' ')
Emojis = {
    ":)": "😊",
    ":(": "😔"
}
Output = ""
for Word in Words:
    Output += Emojis.get(Word, Word) + " "
print(Output)
