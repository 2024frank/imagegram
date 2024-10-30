# This program calculates how many hours a TV series will take to watch.

# 1. Get the number of minutes, episodes, and seasons from the user

minutes = int(input("How many minutes per episode? "))
episodes = int(input("How many episodes in each season? "))
seasons = int(input("How many seasons are there to watch? "))

# 2. Calculate the total number of hours

total_hours = (minutes*episodes*seasons)/60

# 3. Convert the hours to weeks, days, and leftover hours
week = int(total_hours//168)
remaining_hours = total_hours%168
days = int(remaining_hours//24)

hours = int(remaining_hours%24)

# 4. Print the results to the use
print("It will take", total_hours, "hours", "to watch this TV series, which is:",str(week),"week(s),", str(days),"day(s),", "and ",str(hours),"hour(s)")
