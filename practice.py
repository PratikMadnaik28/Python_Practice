command = ""

Started = False
while True:
    command = input("> ")
    if command == "Start":
        if Started:
            print("Car is already started")
        else:
            Started = True
            print("Car is started")
    elif command == "Stop":
        if not Started:
            print("Car is already stopped")
        else:
            Started = False
            print("Car is stopped")
    elif command == "Help":
        print("""
Start - To start the car
Stop - To stop the car
Quit - To quit the game""")
    elif command == "Quit":
        break
else:
    print("Sorry, I don't understand")
