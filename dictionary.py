'''vac = {
    "name": "Dyson V15 Cordless Vacuum",
    "price": 699.99,
    "department": "Appliances",
    "description": "High-powered cordless vacuum with laser dust detection."
}


print(vac["name"], vac["price"])'''

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
        "department":"Produce"
        "description" "Food for purchase"
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

y=input("What would you like")

def whatitem(items):
    if y=="Nvidia" or "RTX" or"0":
        print(Williams_Items[0])
    elif y=="milk" or "1":
        print(Williams_Items[1])
    elif y=="Kevins monitor" or "2":
        print(Williams_Items[2])
    elif y=="Buy one get one free deal" or "Glasses"or"3":
        print(Williams_Items[3])
whatitem(y)