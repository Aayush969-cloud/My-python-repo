# Calculator using python which perform basic unit tasks like addition,subtraction,multiplyand divide using two no.

print("Welcome:) ")

def add(x,y):
    return x + y
def sub(x,y):
    return x - y 
def mul(x,y):
    return x * y 
def div(x,y):
    return x / y  


print("1:addition /n 2: substraction /n 3: multiply /n 4:division")
user_choice = int(input("Enter your choise 1/2/3/4: "))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if user_choice == 1:
    print(num1 , "+" , num2 , "=" , add(num1,num2))
elif user_choice == 2:
    print(num1 , "-" , num2 , "=" , sub(num1,num2))    
elif user_choice == 3:
    print(num1 , "*" , num2 , "=" , mul(num1,num2))
elif user_choice == 4:
    print(num1 , "/" , num2 , "=" ,  div(num1,num2))    
else:
    print("Invalid input")    




