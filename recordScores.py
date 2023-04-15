import RPi.GPIO as GPIO
import requests
import time
import random
from RPLCD.i2c import CharLCD

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.IN)
GPIO.setup(29, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

# Initialize the LCD display
lcd = CharLCD('PCF8574', 0x27)

userIds = [
    '6431ad39a9b0891674d62703', 
    '6431b5665d2f022b78b4845a', 
    '6432a73e4101583ff0d1b61e', 
    '6432a7824101583ff0d1b622', 
    '6432a7994101583ff0d1b625', 
    '6432a7a64101583ff0d1b628'
]

scores = []

while True:
    if len(scores) < 10:
        if len(scores) < 2:
            angle = 30
        elif len(scores) < 4:
            angle = 60
        elif len(scores) < 6:
            angle = 90
        elif len(scores) < 8:
            angle = 120
        else:
            angle = 150
            
        if GPIO.input(31) == GPIO.LOW:
            scores.append([angle, 10, 1])
            print(scores)  # Print the scores array after adding a score
            lcd.clear()  # Clear the display
            lcd.write_string("[{}, {}, {}]".format(angle, 10, 1))  # Write the score data to the display
            time.sleep(1)  # Wait for 5 seconds before adding another score
        elif GPIO.input(29) == GPIO.LOW:
            scores.append([angle, 10, 2])
            print(scores)  # Print the scores array after adding a score
            lcd.clear()  # Clear the display
            lcd.write_string("[{}, {}, {}]".format(angle, 10, 2))
            time.sleep(1)  # Wait for 1 second before adding another score
        elif GPIO.input(11) == GPIO.LOW:
            scores.append([angle, 10, 3])
            print(scores)  # Print the scores array after adding a score
            lcd.clear()  # Clear the display
            lcd.write_string("[{}, {}, {}]".format(angle, 10, 3))
            time.sleep(1)  # Wait for 1 second before adding another score
        elif GPIO.input(13) == GPIO.LOW:
            scores.append([angle, 10, 4])
            print(scores)  # Print the scores array after adding a score
            lcd.clear()  # Clear the display
            lcd.write_string("[{}, {}, {}]".format(angle, 10, 4))
            time.sleep(1)  # Wait for 1 second before adding another score
        elif GPIO.input(15) == GPIO.LOW:
            scores.append([angle, 10, 5])
            print(scores)  # Print the scores array after adding a score
            lcd.clear()  # Clear the display
            lcd.write_string("[{}, {}, {}]".format(angle, 10, 5))
            time.sleep(1)  # Wait for 1 second before adding another score

    else:
        loading = True
        while loading:
            try:
                print("Sending scores to server...")
                lcd.clear()  # Clear the display
                lcd.write_string("Sending Scores")
                userId = random.choice(userIds)
                response = requests.post('https://aimassist-server.onrender.com/api/v1/round/postRound', json={'scores': scores, 'userId': userId})
                if response.status_code == 200:
                    print("Response received! Start shooting again to send another response")
                    lcd.clear()  # Clear the display
                    lcd.write_string("Scores Sent! Start Shooting")
                    scores = []  # Clear the array if the POST request was successful
                    loading = False
                else:
                    print("Error: ", response.status_code)
            except:
                print("Error: Could not connect to server.")
            time.sleep(1)  # Wait for 1 second before trying again
