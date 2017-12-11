# CTI-110 
# M3HW2- SOFTWARE SALES
# JOE FRYE   
# 9/24/17

Q=int(input(" please enter your quantity:"))

packageprice=99

if Q<10:
    discount=0

elif Q<20:
    discount=0.10
    
elif Q<50:
    discount=0.20
    
elif Q<100:
    discount=0.30

else:
    discount=0.40


subtotal=Q*packageprice
discountamount=discount*subtotal
total=subtotal-discountamount

print("amount of discount:"+ format(discountamount,",.2f"))

print("your total is:"+format(total,",.2f"))

