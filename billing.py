x=input("Enter customer name:")
print(x)
print("Menu")
Rate=["Paneer:200","Vegpulav:100","Tandoori:250"]
print(Rate)

print("##########################################################")

print("Quantity of food")
Paneer=int(input("Paneer:"))
Vegpulav=int(input("Vegpulav:"))
Tandoori=int(input("Tandoori:"))

if (Paneer==0 and Vegpulav==0 and Tandoori==0):
    print("Nothing ordered")
elif(Paneer==0 and Vegpulav==0 and Tandoori==1):
    print("Ordered Tandoori")
elif(Paneer==0 and Vegpulav==1 and Tandoori==1):
    print("Ordered Vegpulav and Tandoori")
elif(Paneer==1 and Vegpulav==1 and Tandoori==1):
    print("Ordered Paneer,Vegpulav and Tandoori")

elif(Paneer==0 and Vegpulav==1 and Tandoori==0):
    print("Ordered Vegpulav")
elif(Paneer==1 and Vegpulav==0 and Tandoori==1):
    print("Ordered Paneer and Tandoori")


elif(Paneer==1 and Vegpulav==0 and Tandoori==0):
    print("Ordered Paneer")
elif(Paneer==1 and Vegpulav==1 and Tandoori==0):
    print("Ordered Paneer and Vegpulav")

print("###############################################################")

Paneer_1=Paneer*200
print("Paneer=")
print(Paneer_1)
Vegpulav_2=Vegpulav*100
print("Vegpulav=")
print(Vegpulav_2)
Tandoori_3=Tandoori*250
print("Tandoori=")
print(Tandoori_3)

Cost=Paneer_1+Vegpulav_2+Tandoori_3
print("Your amount is")
print(Cost)

print("##############################################################")
if (Cost>1000):
    print("You get 20% discount")

(Discount=Cost-Cost*20/100
print("Total Amount after discount")
print(Discount)
print("You have to pay Rs.")
print(Discount)

print("###############################################################")
print("Thanks for Visiting")
