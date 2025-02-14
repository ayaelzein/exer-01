age = int(input("Please enter your age: "))

if age <= 10:
    print("Your total will be 5 dollars")
elif 10 < age < 70:
    print("Your total will be 10 dollars")
elif age >= 70:
    print ("You'll get the early bird discount, so your total will be 5 dollars")