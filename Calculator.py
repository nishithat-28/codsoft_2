print(".....................CALCULATOR.....................\n")

while True:
    print("-------------------------------------------------")
    print("Operations: \n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")
    ch=int(input("Enter your choice: "))
    l=["+","-","*","/"]

    try:
        a=input("Enter number 1: ")
        b=input("Enter number 2: ")
        res=eval(a+l[ch-1]+b)

    except IndexError:
        print("Invalid choice!\n")
        pass

    except TypeError:
        print("Invalid numbers!\n")
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
