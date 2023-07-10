import datetime

# Get start time from user input
start_time_str = input("Enter start time (hh:mm): ")
start_time = datetime.datetime.strptime(start_time_str, "%H:%M")

# Get time to add from user input
time_to_add_str = input("Enter time to add (hh:mm): ")
time_to_add = datetime.datetime.strptime(time_to_add_str, "%H:%M")

# Calculate end time
end_time = start_time + datetime.timedelta(hours=time_to_add.hour, minutes=time_to_add.minute)

# Print results
print(f"Start time: {start_time.strftime('%H:%M')}")
print(f"Time to add: {time_to_add.strftime('%H:%M')}")
print(f"End time: {end_time.strftime('%H:%M')}")
