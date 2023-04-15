import requests
import RPi.GPIO as GPIO
import time

# Define the API endpoint URL
url = 'https://aimassist-server.onrender.com/api/v1/main/postRound'

# Define the LDR pins and their associated points
ldr_pins = [17, 18, 27, 22, 23]
ldr_points = [1, 2, 3, 4, 5]

# Set up the GPIO pins for input
GPIO.setmode(GPIO.BCM)
for pin in ldr_pins:
    GPIO.setup(pin, GPIO.IN)

# Initialize the scores array and hit counter
scores = []
hit_count = 0

# Loop until 10 hits have been recorded
while hit_count < 10:
    # Check each LDR pin for a hit
    for i, pin in enumerate(ldr_pins):
        if GPIO.input(pin) == GPIO.HIGH:
            # Record the associated points and increment the hit counter
            score = ldr_points[i]
            scores.append(score)
            hit_count += 1
            print(f'Hit {hit_count} - score: {score}')
            if hit_count >= 10:
                break
    # Wait for a short time before checking again
    time.sleep(0.1)

# Define the request headers and payload
headers = {'Content-Type': 'application/json'}
payload = {'scores': scores}

# Send the POST request with the payload
response = requests.post(url, headers=headers, json=payload)

# Check the response status code
if response.status_code == 200:
    print('Scores posted successfully!')
else:
    print('Error posting scores:', response.content)

# Clean up the GPIO pins
GPIO.cleanup()
