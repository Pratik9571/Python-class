
#! Question 1
# num = [1,3,5,12,17,25,89]

# for i in num:
#     if i>50:
#         break
#     if i%5==0:
#         continue
#     print(i)

#! Question 2
# password = input("Enter your password: ")

# containLetter = 0
# containDigit = 0
# containSpecial = 0

# for char in password:
#     if char.isalpha():
#         containLetter=1
#     elif char.isdigit():
#         containDigit = 1
#     elif char in "@#$%&":
#         containSpecial=1
        
# if len(password) < 6 or (containLetter and not containDigit and not containSpecial):
#     print("Password Strength: Weak")
# elif len(password) >= 6 and containLetter and containDigit:
#     if len(password) >= 8 and containSpecial:
#         print("Password Strength: Strong")
#     else:
#         print("Password Strength: Moderate")

#! Question 3

# sentence = input("Enter a sentence: ")

# words = sentence.split()
# new_words = []

# for i in range(len(words)):
#     if i % 2 == 1:  
#         new_words.append(words[i][::-1])  
#     else:
#         new_words.append(words[i])  

# new_sentence = " ".join(new_words)
# print("New sentence:", new_sentence)

#! Question 4

# words = ["apple", "banana", "apple", "orange", "banana", "banana"]
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1  
#     else:
#         word_count[word] = 1  

# duplicates = {}

# for word in word_count:
#     if word_count[word] > 1:  
#         duplicates[word] = word_count[word]

# print(duplicates)

#! Question 5
# books = {
#     'Book1': 5,
#     'Book2': 6,
#     'Book3': 10,  
# }
# print(books)

#! Question 6
# books = {
#     'Book1': 5,
#     'Book2': 6,
#     'Book3': 10 
# }

# bookName = input("Enter the name of the book you want: ")

# if bookName in books:
#     while True:
    
#         copiesWanted = input("Enter the number of copies you want to buy: ")
        
    
#         if copiesWanted.isdigit():
#             copies_wanted = int(copiesWanted)
#             break 
#         else:
#             print("Invalid input. Please enter a valid number.")


#     if copies_wanted <= books[bookName]:
#         print("Available")
#     else:
#         print("Partially Available")
# else:
#     print("Unavailable")

#! Question 7
# words = ["This", "is", "good", "is"]

# wordCount = {}

# for word in words:
#     wordLower = word.lower() 
#     if wordLower in wordCount:
#         wordCount[wordLower] += 1 
#     else:
#         wordCount[wordLower] = 1 

# print(wordCount)
