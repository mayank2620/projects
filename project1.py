2print("""1. HORIZONTAL
2.VERTICAL""")
a=int(input("ENTER YOUR CHOICE:"))#choice for representatio
if(a==1 or a==2):
    print("""1. ASCENDING
2. DESCENDING""")
    b = int(input("ENTER YOUR CHOICE:"))  # choice for arrangement
    if(b==1 or b==2):
        c=int(input("ENTER STARTING POINT:"))
        d=int(input("ENTER ENDING POINT:"))
        e=int(input("ENTER A GAP FOR NUMBERS:"))

        if(a==1 and b==1):#HORIZONTAL AND ASCENDING
            for i in range(c,d+1,e):
                print(i)

        elif(a==2 and b==1):#VERTICAL AND ASCENDING
            for i in range(c,d+1,e):
                print(i,end=' ')

        elif(a==1 and b==2):#HORIZONTAL AND DESCENDING
            for i in range(c,d+1,-e):
                print(i)

        elif(a==2 and b==2):#VERTICAL AND DESCENDING
            for i in range(c,d+1,-e):
                print(i,end=' ')

    else:
        print("!!!WRONG CHOICE!!!")

else:
    print("!!!WRONG CHOICE!!!")


