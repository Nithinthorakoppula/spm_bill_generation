from datetime import datetime

name=input("enter your name:")

lists='''
rice    rs 20/kg
sugar   rs 30/kg
salt    rs 20/kg
oil     rs 80/kg
paneer  rs 60/kg
maggi   rs 50/kg
boost   rs 90/kg
colgate rs 40/kg
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items={"rice":20,
"sugar":30,
"salt":20,
"oil":80,
"paneer":60,
"maggi":50,
"boost":90,
"colgate":40}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy 1or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter the quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry your item is not here") 
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass 
        if finalamount!=0:
            print(25*"=","nithin super market",25*"=")
            print(28*" ","nalgonda")
            print("name:",name,30*" ","date:",datetime.now())
            print(75*"-")
            print("sno",8*" ","items",8*" ","quantity",3*" ","price",3*" ")
            for i in range(len(pricelist)):
                print(i,8*' ',2*" ",ilist[i],8*' ',3*" ",qlist[i],6*" ",plist[i],3*" ")
            print(75*'-')
            print(50*" ",'totalamount:',"rs",totalprice)
            print("gst amount:",50*" ",'rs',gst)
            print(75*"-")
            print(50*" ","finalamount","rs",finalamount)
            print(75*"-")
            print(50*" ","thaks for visting us")