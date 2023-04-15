import RPi.GPIO as GPIO
import time

# Set up GPIO pins
LDR1_PIN = 3
LDR2_PIN = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LDR1_PIN, GPIO.IN)
GPIO.setup(LDR2_PIN, GPIO.IN)

# Infinite loop to read LDRs
while True:
    # Check LDR1
    if GPIO.input(LDR1_PIN) == GPIO.LOW:
        print("LDR1")
    # Check LDR2
    if GPIO.input(LDR2_PIN) == GPIO.LOW:
        print("LDR2")

    # Delay for a short amount of time
    time.sleep(0.1)
