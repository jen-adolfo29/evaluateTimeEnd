hour = int(input("Starting time (hours): "))
minutes = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# find a total of all minutes
minutes = minutes + dura

# find a number of hours hidden in minutes and update the hour
hour = hour + minutes // 60

# correct minutes to fall in the (0..59) range
minutes = mins % 60

# correct hours to fall in the (0..23) range
hour = hour % 24

print(hour, ":", mins, sep='')