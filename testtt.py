x=int(input("Enter your number: "))

def fib(n):
    a=0
    b=1

    if n<=0:
        print("Please try again. ")

    elif n>=100:
        print("Bye Bye")
        breakpoint(0,0)

    elif n==1:
        print(a)

    else:
        print(a)
        print(b)



fib(x)
