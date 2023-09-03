print("WELCOME, WE ARE HERE TO PROVIDE SERVICE")
takeInput = int(input("Enter your budget: "))

if (200 >= takeInput >= 100):
    print("Please increase your budget")

elif (takeInput >= 201):
    if (201 <= takeInput <= 350):
        print("Local item available in this price", takeInput)
    elif (takeInput >= 350 and takeInput <= 500):
        print("Standard item available in this price", takeInput)
    elif(takeInput>=501 and takeInput<=1000):
        print("Professional item available in this price", takeInput)
    elif(takeInput>=1001 and takeInput<=3000):
        print("Top class item are available in this price", takeInput)
    elif(takeInput>=3001 and takeInput<=5000):
        print("Foregner item are available in this price", takeInput)
    else:
        print("Rushian item are available in this price", takeInput)

    takeInput = input("Are want this item: ")

    if takeInput.lower() == "yes":
        print("Complete your payment process..............")
        takeInput = int(input("Enter your Atm card no: "))
        print("Item purchase succefully now its your and you can use it")

    else:
        print("Thanks for show your interest")

else:
    print("NO item available in this price", takeInput)










