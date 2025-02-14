# print ("Hello World")

# c = 6
# d=11
# print(c+d)


# a = str(6)
# b= str(10)
# print (a + b)

# a= input("Enter the first name:")
# b = input("Enter the last name:  ")

# c = (a + b)
# print("The name of the person is ", c )


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a>c:
    print("The largest number is: ",a )
elif b>a and b>c:
    print("The largest number is: ",b )
else:
    print("The largest number is: ",c )



for num in range(1,21):
    if num%2 == 0:
        print("Even numbers: ", num)

