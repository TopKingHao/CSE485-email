import matplotlib.pyplot as plt

# Lists to store data
water_distance = []
tds_ppm = []

# Read the file
with open("sensorHistory.txt", "r") as file:
    lines = file.readlines()

# Extract data from each line
for line in lines:
    data = line.split("\t")
    for item in data:
        if item.startswith("Water distance in inches"):
            water_distance.append(int(item.split(":")[1]))
        elif item.startswith("TDS PPM"):
            tds_ppm.append(int(item.split(":")[1]))

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(water_distance, label='Water distance in inches', marker='o')
plt.plot(tds_ppm, label='TDS PPM', marker='o')

# Customizing the graph
plt.xlabel('Data Points')
plt.ylabel('Value')
plt.title('Sensor Data History')
plt.legend()
plt.tight_layout()

# Show the graph
plt.show()
