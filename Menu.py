menu={"espresso":
      {"ingredients":{
          "water":50,
          "coffee":18
          },
          "cost":1.5
          },
      "latte":{
        "ingredients":{
          "water":200,
          "milk":150,
          "coffee":150
          },
          "cost":2.5
      },
      "cappuccino":{
        "ingredients":{
          "water":250,
          "milk":100,
          "coffee":24
          },
          "cost":3.0
      }
  }

resources={
    "water":300,
    "milk":200,
    "coffee":100
}

profit=0

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("please insert coins : ")
    total=int(input("how many quarters?: "))*0.25
    total +=int(input("how many dimes?: "))*0.1
    total +=int(input("how many nickles?: "))*0.05
    total +=int(input("how many pennies?: "))*0.01
    return total


def is_transaction_successful(moneyrecd,drinkcost):
    if moneyrecd>=drinkcost:
        change=round(moneyrecd-drinkcost , 2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drinkcost
        return True
    else:
        print("Sorry thats not enough money . Money refunded.")
        return False
    

def make_coffee(drinkname,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drinkname}")
    


is_on=True
while is_on:
    choice = input("What would you want espresso,latte or cappuccino ? :")
    if choice =="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")      
        print(f"Money: ${profit}")

    else: 
        drink=menu[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])