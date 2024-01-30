import datetime

# Get the current time
current_time = datetime.datetime.now()

# Format the time as a string
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Open the text file in write mode and write the formatted time
with open("runtime.txt", "w") as file:
    file.write(formatted_time + "\n")

print("Current time written to 'runtime.txt'")
