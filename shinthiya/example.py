user = 'raju110'
password = 'RAJU110'
choice = int(input('What do u want to do?  1.Addition, 2.Subtraction, 3.Multiplication, 4.Division, 5.Power (1, 2, 3, 4, 5): '))

x =input("enter your username:")

y =input("enter your password:")
if user==x and password==y:
    print("success your login") 
    
    if choice == 1:
        def addition(x,y):
            sum=x+y
            print(sum)
        addition(5,4) 
    elif choice == 2:
        def subtraction(x, y):
            sub = x - y
            print( sub)
        subtraction(10, 4)  
    elif choice == 3:
        def multiplication(x, y):
            mul = x * y
            print( mul)
        multiplication(4, 3)

    elif choice == 4:
        def division(x, y):
            if y == 0:
                print("Cannot divide by zero")
            else:
                div = x / y
                print( div)
        division(14, 2)

    elif choice == 5:
        def power(x):
            pow = x ** 3
            print( pow)
        power(3)

    else:
        print("Invalid choice")

else:
    print("Login failed. Please check your username and password.")