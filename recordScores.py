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
userId = ''
scores = []


while True:
    try:
        session_data = requests.get(
            'https://aimassist-server.onrender.com/api/v1/session/getsession?device=1').json()
        session_started = session_data['data']['session_started']
        userId = session_data['data']['userid']
        sessionId = session_data['data']['_id']
        distance = session_data['data']['distance']
        email = session_data['data']['email']
        
    except:
        session_started = False
        

    if session_started: 
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
                scores.append([angle, distance, 1])
                print(scores)  # Print the scores array after adding a score
                lcd.clear()  # Clear the display
                # Write the score data to the display
                lcd.write_string("[{}, {}, {}]".format(angle, distance, 1))
                # Wait for 1 seconds before adding another score
                time.sleep(1)
            elif GPIO.input(29) == GPIO.LOW:
                scores.append([angle, distance, 2])
                print(scores)  # Print the scores array after adding a score
                lcd.clear()  # Clear the display
                lcd.write_string("[{}, {}, {}]".format(angle, distance, 2))
                # Wait for 1 second before adding another score
                time.sleep(1)
            elif GPIO.input(11) == GPIO.LOW:
                scores.append([angle, distance, 3])
                print(scores)  # Print the scores array after adding a score
                lcd.clear()  # Clear the display
                lcd.write_string("[{}, {}, {}]".format(angle, distance, 3))
                # Wait for 1 second before adding another score
                time.sleep(1)
            elif GPIO.input(13) == GPIO.LOW:
                scores.append([angle, distance, 4])
                print(scores)  # Print the scores array after adding a score
                lcd.clear()  # Clear the display
                lcd.write_string("[{}, {}, {}]".format(angle, distance, 4))
                # Wait for 1 second before adding another score
                time.sleep(1)
            elif GPIO.input(15) == GPIO.LOW:
                scores.append([angle, distance, 5])
                print(scores)  # Print the scores array after adding a score
                lcd.clear()  # Clear the display
                lcd.write_string("[{}, {}, {}]".format(angle, distance, 5))
                # Wait for 1 second before adding another score
                time.sleep(1)
        else:
            loading = True
            while loading:
                try:
                    print("Sending scores to server...")
                    lcd.clear()  # Clear the display
                    lcd.write_string("Sending Scores")
                    response = requests.post(
                        'https://aimassist-server.onrender.com/api/v1/round/postRound', json={'scores': scores, 'userId': userId, 'email': email})
                    if response.status_code == 200:
                        sessionResponse = requests.post(
                            'https://aimassist-server.onrender.com/api/v1/session/endsession', json={'sessionId' : sessionId})
                        if sessionResponse.status_code == 200:                                
                            print("Response received! Start session again to send another response")
                            lcd.clear()  # Clear the display
                            lcd.write_string("Scores Sent! Start session")
                
                            scores = []  # Clear the array if the POST request was successful
                            session_started = False
                            userId = ''
                            sessionId = ''
                            distance = ''
                            loading = False
                        else: 
                            print("Error: ", sessionResponse.status_code)
                    else:
                        print("Error: ", response.status_code)
                except:
                    print("Error: Could not connect to server.")
                time.sleep(1)  # Wait for 1 second before trying again
    elif not session_started:
        if GPIO.input(31) == GPIO.LOW:
            print('Start session before shooting')
            lcd.clear()  # Clear the display
            lcd.write_string("Start Session")
            time.sleep(1)
        elif GPIO.input(29) == GPIO.LOW:
            print('Start session before shooting')
            lcd.clear()  # Clear the display
            lcd.write_string("Start Session")
            time.sleep(1)
        elif GPIO.input(11) == GPIO.LOW:
            print('Start session before shooting')
            lcd.clear()  # Clear the display
            lcd.write_string("Start Session")
            time.sleep(1)
        elif GPIO.input(13) == GPIO.LOW:
            print('Start session before shooting')
            lcd.clear()  # Clear the display
            lcd.write_string("Start Session")
            time.sleep(1)
        elif GPIO.input(15) == GPIO.LOW:
            print('Start session before shooting')
            lcd.clear()  # Clear the display
            lcd.write_string("Start Session")
            time.sleep(1)
    