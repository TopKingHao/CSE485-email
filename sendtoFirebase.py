import pyrebase
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# Configure your Firebase project
config = {
	"apiKey": "AIzaSyCQx53E_31CuN2INeyph8n14gvpoLA-PAo",
	"authDomain": "automatic-hydroponic-sys.firebaseapp.com",
	"databaseURL": "https://automatic-hydroponic-sys-default-rtdb.firebaseio.com",
	"storageBucket": "automatic-hydroponic-sys.appspot.com"
}



# Initialize Firebase
firebase = pyrebase.initialize_app(config)

# Access the Database Service
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("----------------------------------------")
print()
while True:
    
    #-----------------------
    # Define variables to store values
    waterdist = 0
    TDSP = 0

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
    #------------------------
    
    #check for unnacceptable reading on sensor, possibly send alert email
    def sendAlert(file_path):
        try:
            with open(file_path, 'r') as file:
                python_code = file.read()
                exec(python_code)
        except FileNotFoundError:
            print("Error: The file does not exist.")
      
    file_path ='sendemail.py'
    
    file_path2 ='sendemailTDS.py'
    
    
    if(waterdist>40):
        sendAlert(file_path)   
        
    if(TDSP<100):
        sendAlert(file_path2)   
    
    #check for unnacceptable reading end
    
    
    
    
    
    
    
    
    tlcdata = waterdist
    ppmdata = TDSP
    print("Ultrasonic Sensor: {} C".format(tlcdata))
    print("PPM Sensor: {} C".format(ppmdata))
    print()
    data = {
        "Ultrasonic Sensor": tlcdata,
        "PPM Sensor": ppmdata,
    }
    db.child("SensorData").child("Ultrasonic Sensor").set(tlcdata)
    db.child("SensorData").child("PPM Sensor").set(ppmdata)

		
    time.sleep(30)
