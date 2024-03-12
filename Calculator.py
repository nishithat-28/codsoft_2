print(".....................CALCULATOR.....................\n")
while True:
    print("-------------------------------------------------")
    a=input("Enter number 1: ")
    b=input("Enter number 2: ")
    print("Operations: \n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")
    ch=int(input("Enter your choice: "))
    l=["+","-","*","/"]
    try:
        res=eval(a+l[ch-1]+b)
    except:
        print("Invalid numbers or choice!\n")
        pass
    else:
        print("{} {} {} = {}\n".format(a,l[ch-1],b,res))
    finally:
        x=(input("Calculate again? (Yes/No): ")).lower()
        if x=="yes":
            pass
        else:
            break

print("....................................................")
