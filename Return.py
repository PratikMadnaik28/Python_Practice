def emojis_converter(Message):
    Words = Message.split(' ')
    Emojis = {
        ":)": "😊",
        ":(": "😔"
    }
    Output = ""
    for Word in Words:
        Output += Emojis.get(Word, Word) + " "
    return Output

Message = input("> ")
print(emojis_converter(Message))
