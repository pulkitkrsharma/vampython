#we have to use if else condition for decision making in python
#check you are eligible for voting or not
#get the age from user
userAge = int(input("Enter your age"))
#to check the user is eligible for voting then check age must be greater than 18

# if userAge > 18:
#     print("You'r eligible for voting")
# else:
#     print("You'r not eligible for voting")

#check the user is eligible for vote and super vote
#super vote age should be greater than 55
#vote age should be greater than 18 less than 55
if userAge > 18 and userAge < 55:
    print("You'r eligible for voting")
elif userAge > 55:
    print("You'r eliglible for super vote")
else:
    print("You'r not eliglible for voting")  
