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
cart=[]

print(Williams_Items)
def whatitem():
    while True:
        y=input("Would you like to shop('1)exit' to leave, '2)continue to shop' 3) 'go to cart'4)Checkout )")
        if y=="1":
            print("Have a good day")
            break
        if y=="2":
            x=input("What would you like to do('a)exit' to leave, 'b)continue to shop' c) 'go to cart'd)Checkout )")
            print(Williams_Items[0]["name"])
            print(Williams_Items[0]["price"])
            print(Williams_Items[0]["department"])
            if x.lower()=="yes":
                cart.append(Williams_Items[0])
                print("Item added")
            else:
                print("Item not added")
            x=input("What would you like to do('a)exit' to leave, 'b)continue to shop' c) 'go to cart'd)Checkout )")
            print(Williams_Items[1]["name"])
            print(Williams_Items[1]["price"])
            print(Williams_Items[1]["department"])
            if y=="a":
                print("Have a good day")
                break
            if y=="c":
                 print(cart["name","price"])
            if y=="b":
                if x.lower()=="Yes":
                    cart.append(Williams_Items[1])
                    print("Item added")
                else:
                    print("Item not added")
            x=input("What would you like to do('a)exit' to leave, 'b)continue to shop' c) 'go to cart'd)Checkout )")
            print(Williams_Items[2]["name"])
            print(Williams_Items[2]["price"])
            print(Williams_Items[2]["department"])
            if y=="a":
                print("Have a good day")
                break
            if y=="c":
                print(cart["name","price"])
            if y=="b":
                if x.lower()=="Yes":
                    cart.append(Williams_Items[2])
                    print("Item added")
                else:
                    print("Item not added")
            x=input("What would you like to do('a)exit' to leave, 'b)continue to shop' c) 'go to cart'd)Checkout )")
            print(Williams_Items[3]["name"])
            print(Williams_Items[3]["price"])
            print(Williams_Items[3]["department"])
            if y=="a":
                print("Have a good day")
                break
            if y=="c":
                print(cart["name","price"])
            if y=="b":
                if x.lower()=="Yes":
                    cart.append(Williams_Items[3])
                    print("Item added")
                else:
                        print("Item isn't added")
        if y=="3":
            for item in cart:
                print(cart["name","price"])
            if cart==" ":
                 print("Nothing here")
        total=0
        if y=="4":
            for item in cart:
                print(cart["name","price"])
                total+=cart["price"]
                print(cart["name"])
whatitem()
            


'''print(Williams_Items[4]["name"])
                print(Williams_Items[4]["price"])
                print(Williams_Items[4]["department"])
                x==input("Do you want it?")
                if x.lower=="Yes" or"yes":
                     cart.append(Williams_Items[4])
        
            
        if y=="Nvidia" or "RTX" or"0":
            print(Williams_Items[0])
            history.append(y)
        if y=="milk" or "1":
            print(Williams_Items[1])
            history.append(y)
        if y=="Kevins monitor" or "2":
            print(Williams_Items[2])
            history.append(y)
        if y=="Buy one get one free deal" or "Glasses"or"3":
            print(Williams_Items[3])
            history.append(Williams_Items["price"])
        p=input("are you sure")
        if p=="yes" or "Yes":
            history.append(y)
        if p=="No" or"no":
            print(Williams_Items[all])
whatitem()'''
