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
while True:
    def whatitem():
        show_items(Williams_Items)
        print(Williams_Items[y])
        cart.append(Williams_Items(selected_number))
        y=input("What number")
    for i in range(item):
        selected_number=y
        finish=input("are you done shopping(If yes) type Y, if you want to continue, type C").upper()
        if finish=="Y":
            item=Williams_Items[selected_number]
            total=+item
            cart.append(item)
            break
        elif finish=="N":
            y=input("WHat number item would you like?")


