# Define variables to store values
waterdist = None
TDSP = None

# Read the file
with open("sensorHistory.txt", "r") as file:
    lines = file.readlines()

# Extract values from the second-to-last line
if len(lines) >= 2:
    penultimate_line = lines[-2].strip()  # Get the second-to-last line
    data = penultimate_line.split("\t")   # Split line by tabs
    for item in data:
        if item.startswith("Water distance in inches"):
            waterdist = int(item.split(":")[1])
        elif item.startswith("TDS PPM"):
            TDSP = int(item.split(":")[1])

# Display the values
print(waterdist)
print(TDSP)

