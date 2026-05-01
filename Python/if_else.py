# if statment are basically conditional statments it executes if the condition meets
# otherwise else statment is executed 

# age = 33

# if then the conditon :
#     executable code  
# else:
#     in case if is not executed then this will execute code

age =int(input("Enter your age: "))

if age > 18:
    print("You can drive")
else:
    print("You can not drive")

# in case if statment is not met and you want to put mroe statment there
# so you can use elif statment to add multiple if statment if one elif statment is met then the lader will break 
# and if no one is met it will go to the else statment

marks = int(input("Enter your marks obtained:"))

if marks == 100:
    print("You got the best marks there")
elif marks >= 90:
    print("you achieved A+")
elif marks >= 90:
    print("you got B+")
else :
    print("you need to work hard")