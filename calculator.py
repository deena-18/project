'''
def display_menu():
    print("\n---caluculator menu---")
    print("1.Addition")
    print("2.Subtraction")
    print("3.multiplication")
    print("4.Division")
    print("5.Exit")
    return input("choose an operation(1-5):")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return(a*b)
def divide(a,b):
    if b==0:
        return"error:Division by zero is undefined"
        return a/b
while True:
    choice=display_menu()
    if choice in["1","2","3","4"]:
        try:
            num1=float(input("enter tne first number:"))
            num2=float(input("enter the second number:"))
            if choice=="1":
                result=add(num1,num2)
                print(f"result:{num1}+{num1}={result}")
            elif choice=="2":
                result=subtract(num1,num2)
                print(f"result:{num1}-{num2}={result}")
            elif choice=="3":
                result = multiply(num1, num2)
                print(f"result:{num1}*{num1}={result}")
            elif choice == "4":
                result=divide(num1, num2)
                print(f"result:{num1}/{num1}={result}")
        except ValueError:
            print("invalid input! please enter number only")
    elif choice=="5":
        print("Exiting the calculator.goodbye!")
        break
    else:
        print("invalid choice! please select a valis operation)")
'''
output:
---caluculator menu---
1.Addition
2.Subtraction
3.multiplication
4.Division
5.Exit
choose an operation(1-5):1
enter tne first number:7889
enter the second number:85749
result:7889.0+7889.0=93638.0

---caluculator menu---
1.Addition
2.Subtraction
3.multiplication
4.Division
5.Exit
choose an operation(1-5):2
enter tne first number:78759
enter the second number:6847
result:78759.0-6847.0=71912.0

---caluculator menu---
1.Addition
2.Subtraction
3.multiplication
4.Division
5.Exit
choose an operation(1-5):3
enter tne first number:673683
enter the second number:5784
result:673683.0*673683.0=3896582472.0

---caluculator menu---
1.Addition
2.Subtraction
3.multiplication
4.Division
5.Exit
choose an operation(1-5):4
enter tne first number:6879
enter the second number:48384
result:6879.0/6879.0=None

---caluculator menu---
1.Addition
2.Subtraction
3.multiplication
4.Division
5.Exit
choose an operation(1-5):5
Exiting the calculator.goodbye!
