# Get input from user
year = int(input("Please enter a year: "))

# if the year is a leap year
if ((year%4==0 and year%100!=0) or year%400==0):
	print("The year is a leap year")
# else, the year is NOT a leap year
else:
	if (year%2==0):
		print("The year is NOT a leap year, and the year is even")
	else:
		print("the year is NOT a leap year, and the year is odd")
		



