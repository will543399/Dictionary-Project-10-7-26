Williams_Items= [
    {
        "name":"NVIDIA GeForce RTX 5090",
        "price": 6999.99,
        "department":"Electronics",
        "description":"High quality RTX"

    },
    {

        "name":"Milk",
        "price":10,
        "department":"Produce",
        "description" :"Food for purchase"
    },
    {
        "name":"Kevin's monitor",
        "price":10000,
        "department":"Electronics",
        "description":"Works well enough to give you correct code, but it is used"
    },
    {
        "name":"Buy one get one free Aiden's glasses and Kevin's glasses",
        "price":"One million",
        "department":"Used",
        "description":"From famous people, just very used"

    }
]
cart=[]
total=0
def show_items(items):
    for index, item in enumerate(items):
        print(f'{index},":" (item["name"]')
def whatitem():

        show_items(Williams_Items)
        print(Williams_Items[selected_number])
        cart.append(Williams_Items(selected_number))
while True:
    show_items(Williams_Items)
    y=input("What number")
    selected_number=y
    whatitem()
    finish=input("are you done shopping(If yes) type Y, if you want to continue, type C").upper()
    if finish=="Y":
        total+=sum(item["price"] for item in cart)
        item=Williams_Items[selected_number]
        total=+item
        cart.append(item)
        if cart:
            for item in cart:
                print(item['name'],item['price'])
                print(" ")
            else:
                print("Your cart is empty").lower()
            z=input("Check out????")
            if z=="yes":
                print(" ")
                print("receipt")
                print(" ")
                for item in cart:
                    print(item["name"],item["price"])
                    print(" ")
                    print("Total:"+ float(total))
                    break
                else:
                    print(" ")
    elif finish=="C":
        total+=sum(item["price"]for item in cart)



