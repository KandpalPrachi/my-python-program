from tkinter import Y


print("Are you ready to play?")
option=input("yes/no")

if option=="yes":
    print("lets start...")
else:
    print("see you here soon!!!")


def Add(x,y):
    return x+y
def Subtract():
    return x-Y
def Multiplication():
    return x*Y
def Division():
    return x/y

print("What do you want to play ??")
print("1.Addition")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")

while True:
    choice=input("Enter choice i.e 1,2,3,4")
    
    if choice in ('1', '2', '3', '4'):
        x=int(input('Enter the first number number:'))
        y=int(input('Enter the second number number:'))

        if choice == '1':
            print(x, "+", y, "=", Add(x,y))
        
        elif choice == '2':
            print(x, "-", y, "=", Subtract(x,y))

        elif choice == '3':
            print(x, "*", y, "=", Multiplication(x,y))

        elif choice == '4':
            print(x, "/", y, "=", Division(x,y))



    print("Are you want to play again??")
    again=input("Lets play again? (yes/no):")

    if again == "no":
        break


    else:
        print("Please tap the right button")
 
        



