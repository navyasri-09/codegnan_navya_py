'''
#if statement---this is used to check any condition  if true then it enters the if statement
syntax
if keyword (condition):
    print(statement)
age=int(input("Enter your age:"))
if age>=18:
    print("Your age is 18 or above")
  
stu_att=int(input("Enter sem attendence:"))
if stu_att>=75:
    print("Eligible for the Semester Exam")

age=int(input("Enter your age:"))
if age>=18:
    print("you are Eligible to vote:)

--if-else statement---- fall back statement--executes only when if condition becomes false
if keyword(condition):
    print(statement)
else:
     print(statement)

age=int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote")
else:
    print(f"you can't vote and wait for {18-age} years")

total_amt=int(input("Enter the total amount"))
if total_amt>=149:
     print("No delivery charges")
else:
   print(f"{149-total_amt} to your cart")
   
#if-elif-else---- in the elif part ,i can check another condition----combination of if and if-else

marks=int(input("Enter your Marks:"))
if marks>=90:
    print("You Got A+ Grade")
elif marks>=75:
    print("You Got A Grade")
elif marks>=60:
    print("You Got B Grade")
else:
    print("You are Fail")

    
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
user_choice=input("enter your Choice:\n1.Add,\n2.Sub,\n3.Mul,\n4.Div")
if user_choice== "+":
    print(num1 + num2)
elif user_choice== "-":
    print(num1 - num2)
elif user_choice== "*":
    print(num1 * num2)
elif user_choice== "/":
    print(num1 /num2)

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
user_choice=int(input("enter your Choice:\n1.Add \n2.Sub \n3.Mul \n4.Div \n"))
if user_choice== 1:
    print(num1 + num2)
elif user_choice== 2:
    print(num1 - num2)
elif user_choice== 3:
    print(num1 * num2)
elif user_choice== 4:
    print(num1 /num2)
else:
    print("Entered Choice is invalid")'''

num=int(input("Enter a number:"))
if num==0:
    print(f"Enterd number {num}is zero(0)")
elif num>0:
    print(f"Enterd number {num} is Positive")
else:
    print(f"Enterd number {num} is Negative")






    


