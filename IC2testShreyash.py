import smbus2
import time

# Set the I2C address of your display
address = 0x27

# Initialize the I2C bus
bus = smbus2.SMBus(1)

# Define a function to send commands to the display
def lcd_command(cmd):
    bus.write_byte(address, 0x00) # Set RS low for command mode
    bus.write_byte(address, cmd)
    time.sleep(0.0005) # Wait for command to be processed

# Define a function to send data to the display
def lcd_data(data):
    bus.write_byte(address, 0x40) # Set RS high for data mode
    bus.write_byte(address, data)
    time.sleep(0.0005) # Wait for data to be processed

# Initialize the display
lcd_command(0x38) # 8-bit data, 2-line display, 5x8 font
lcd_command(0x0C) # Display on, cursor off, blink off
lcd_command(0x01) # Clear display

# Write "shreyash" to the display
lcd_data(0x73) # s
lcd_data(0x68) # h
lcd_data(0x72) # r
lcd_data(0x65) # e
lcd_data(0x79) # y
lcd_data(0x61) # a
lcd_data(0x73) # s
lcd_data(0x68) # h
