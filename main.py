MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def transaction():
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total
def is_resource_suff(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i] > resources[i]:
            print("Sorry there are not enough items.")
            return False
    return True
def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print("Thank you, Here is your Coffee☕")
def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved > drink_cost:
        change = money_recieved - drink_cost
        return f"Here is your change {change}"
    else:
        print("There is not enough money. Money refunded")
is_on = True
while is_on:
    choice = input("what do you want? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"Current resource is {water} water, {milk} milk, {coffee} coffee")
    else:
        drink = MENU[choice]
        if is_resource_suff(drink["ingredients"]):
            payment= transaction()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



