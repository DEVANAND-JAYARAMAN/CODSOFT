#Calculator
Number_1=int(input("Enter Number 1: "))
Number_2=int(input("Enter Number 2: "))
Operation=input("""Please type the Math operation to be performed :
+   -->>for Addition
-   -->>for subtraction
*   -->>for multiplication
/   -->>for division
%   -->>for modulus_operation :  """) 
#Answer:
if (Operation == "+"): #addition
    print("Answer of {}+{} is:".format(Number_1,Number_2),Number_1 + Number_2)
elif (Operation == "-"): #subtraction
    print("Answer of {}-{} is:".format(Number_1,Number_2),Number_1 - Number_2)
elif (Operation == "*"): #multiplication
    print("Answer of {}*{} is:".format(Number_1,Number_2),Number_1 * Number_2)
elif (Operation == "/"): #division
    print("Answer of {}/{} is:".format(Number_1,Number_2),Number_1 / Number_2)
elif (Operation == "%"): #modulus
    print("Answer of {}%{} is:".format(Number_1,Number_2),Number_1 % Number_2)
else: #invalid_number
    print("Please type a valid number")
    


