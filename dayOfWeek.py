
# string value representing days of week
listDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(listDays)

listDays[0] = "Domingo"

print(listDays)

# input from question
print("Hello, welcome to days of week!")
dayNum = int(input("Please enter a day number in the week: \n"))

# output the answer
print("Day #", dayNum, " corresponds to ", listDays[(dayNum-1) % len(listDays)])

# tuples are lists that are "frozen"
tuplesDays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(tuplesDays)
tuplesDays[0] = "Domingo"  # generates error

