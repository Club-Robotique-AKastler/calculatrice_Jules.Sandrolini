print("Hello, to perform a calculation you can type: 1 for addition, 2 for soustraction, 3 for multiplication, 4 for division")
z=input()
if z!=1 and z!=2 and z!=3 and z!=4 :
    print("please, enter correct number : 1 , 2 , 3 or 4")
elif z==3 :
    open("multiplication.py")
elif z==4 :
    open("division.py")
elif z==2 :
    open("soustraction.py")
elif z==1 :
    open("addition.py")