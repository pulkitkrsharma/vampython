#data type is used to defined the data in which form

#int data is used to store the numeric type data
#Note in python we don't need to declare the datatype
#We just assign the value in variable
#Variable can store any type of value with type of data
age = 33
name = "Pawan Sharma"
salary = 2599.89

#how to pass the variables inside the print statement
#we have 3 ways to pass the variable in print statement
# print("My name is "+ name + " and salary "+ salary+ " and age "+ age)
#It generate the Type error, reason string only concatenate with string not int
#Solution 1:- replace + by , when data type is not string
print("My name is "+ name + " and salary ", salary, " and age ", age)
#Solution 2: pass the variable in print statement with f {}
print(f"my name is {name} salary is {salary} and age {age}")
#Solution 3: typecast the data into string 
salaryString = str(salary)
ageString = str(age)
print("My name is "+ name + " and salary "+ salaryString+ " and age "+ ageString)

#To find the type of data we need to use type() function
print(type(name))
print(type(age))
print(type(salary))

