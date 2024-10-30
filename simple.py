# This program calculates the interest on savings using the simple interest formula.
principal = int(input("How much would you like to save ? "))
interestRate =float(input("What is your interest rate ? "))
time = int(input("Hoe long are you saving the money? "))

interest = principal * interestRate * time
print("Your interest earned would be", "$"+str(interest)+"!")
