#Typecasting convert one data type to another data types

price = 90.59
print(price)
print(type(price))

#convert to integer
payPrice = int(price)
print(payPrice)
print(type(payPrice))

#convert int to string
amount = 2599
stringAmount = str(amount)
print(stringAmount, " and data type is ",type(stringAmount))

#convert string to int
gender = "male"
#ctrl + / to give the line comment
# genderIntoInt = int(gender)
#convertion not possible because string doesn't have ascii no
# print(gender, " data type is ", genderIntoInt)

#to take the input from user c language scanf
myName = input("Enter your name")
#input function has default return type as str
myAge = int(input("Enter your age"))
print("My name is ", myName , " and age is " , myAge)

#find the age in years when bornYear and currentYear given by user
#currency convertor ruppes to USD :- 1 usd = 84 rs
