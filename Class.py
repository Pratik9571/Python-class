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


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b and a>c:
#     print("The largest number is: ",a )
# elif b>a and b>c:
#     print("The largest number is: ",b )
# else:
#     print("The largest number is: ",c )



# for num in range(1,21):
#     if num%2 == 0:
#         print("Even numbers: ", num)


# def add(a,b):
#     return a+b

# def substract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def division(a, b):
#     if  b == 0 or a == 0:
#         return ("Enter different number else than 0.")
#     return a/b

# first = int(input("Enter first Number: "))
# second = int(input("Enter second Number: "))
# print("Enter 1 for addition, 2 for substraction, 3 for multiplication and 4 for division.")
# operation = int(input("Enter the Operation you want to: "))

# if operation == 1:
#     a = add (first, second)
#     print(a)
# elif operation == 2:
#     a = substract(first, second)
#     print(a)
# elif operation == 3:
#     a = multiply(first, second)
#     print(a)
# elif operation == 4:
#     a = division(first, second)
#     print(a)


# students = {"Sugam" : 70,
#             "Kabi": 60,
#             "Pratik": 99,
#             "Prashant": 50,
#             "Saimon": 48,
#             }
# studentsHighestMarks = max(students, key=students.get)
# print("The student with highest marks is", studentsHighestMarks, "with" , students[studentsHighestMarks], "marks.")

# dict1 = {}
# highest_marks = 0
# for k, v in dict1.items():
#     if v>highest_marks:
#         highest_marks = v
#         name= k
# print(name)
    
    


# def square(a):
#     list2=[]
#     for i in a:
#         squares = i ** 2
#         if squares % 2==0:
#             print("The square is: ", squares)
#         list2.append(squares)   

#     print("The new list is: ", list2)
    
  
# list1 = [2,3,4,5,6,10]   
# square(list1)


class Shape:
     def calculateArea(self):
         return 0
         
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    
    def calculateArea(self):
        return 3.14 * self.radius * self.radius
    

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width 
        
    def calculateArea(self):
        return self.length * self.width
    
    
def main():
    circle = Circle(19)
    rectangle = Rectangle(14, 9)
    
    print("The area of the circle is:", circle.calculateArea())
    print("The area of the rectangle is:", rectangle.calculateArea())
    

main()