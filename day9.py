'''looping statements
for loop:---it is used to iterate over a sequence 
for i in range(1,10):
   print(i)   # i is an initial variable where we never get any error even though we didn't define

range function--this is used to generate numbers over a particular range
range(start,end,step)--step is used to skip a step,it jumps to the particular position

for i in range(0,20,3):
    print(i)

string--> can convert int to string but not string to int and float
any=123
print(str(any))     
print(list(any))
print(tuple(any))
print(float(any))

any="abc"
print(int(any))      "cant convert str to int
print(list(any))
print(tuple(any))
print(float(any))

a=[(1,2),(3,4)]
print(dict(a))

str="navya sri"
print(str[::-1])

#reverse a string without using index
str="navyasri"
empty=""
for j in str:
    empty=j+empty
    print(empty)'''

str="madam"
empty=""
for j in str:
    empty=j+empty
if str==empty:
    print(f"{str},is a palindrome")
else:
    print(f"{str},is not a palindrome")


