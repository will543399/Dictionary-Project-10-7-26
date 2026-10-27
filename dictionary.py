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
history=[]

y=input("Would you like to shop('exit' to leave, 'continue' to shop)")
print(Williams_Items)
def whatitem(items):
    while True:
        if y=="exit":
            print("Have a good day")
            break
        if y=="continue":
            for index, item in enumerate(Williams_Items):
                print(index,item["name","price","department","description"])
        
        
        
        

            
        if y=="Nvidia" or "RTX" or"0":
            print(Williams_Items[0])
            history.append(Williams_Items["price"])
        if y=="milk" or "1":
            print(Williams_Items[1])
            history.append(Williams_Items["price"])
        if y=="Kevins monitor" or "2":
            print(Williams_Items[2])
            history.append(Williams_Items["price"])
        if y=="Buy one get one free deal" or "Glasses"or"3":
            print(Williams_Items[3])
            history.append(Williams_Items["price"])
        p=input("are you sure")
        if p=="yes" or "Yes":
            history.append(y)
        if p=="No" or"no":
            print(Williams_Items[all])
whatitem()