import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Use for I2C.
i2c = board.I2C()
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
# disp.fill(0)
# disp.show()

def wakeup():
    image = Image.open('Images/23-eyes_tired.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.3)

    image = Image.open('Images/26-lower_lids.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.2)
    
    image = Image.open('Images/18-eyes_glare.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.1)

    image = Image.open('Images/01-eyes_distressed.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.1)

    image = Image.open('Images/07-eyes_front.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.1)
#wakeup()

def sleep():
    image = Image.open('Images/07-eyes_front.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.1)

    image = Image.open('Images/01-eyes_distressed.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.1)

    image = Image.open('Images/18-eyes_glare.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.1)

    image = Image.open('Images/23-eyes_tired.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.1)

def dog():
    image = Image.open('Images/dog.jpg').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(image)
    disp.show()
    time.sleep(.1)

# x = 3
# while 1:
#     if x == 1:
#         # Load image based on OLED display height.  Note that image is converted to 1 bit color.
#         image = Image.open('Images/Face1.jpg').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

#     if x == 2:
#         # Load image based on OLED display height.  Note that image is converted to 1 bit color.
#         image = Image.open('Images/01-eyes_distressed.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

#     if x == 3:
#         # Load image based on OLED display height.  Note that image is converted to 1 bit color.
#         image = Image.open('Images/07-eyes_front.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

#     #   Show Image
#     disp.image(image)
#     disp.show()
#     x=x-1
#     if x == 0:
#         x=3
#     time.sleep(.4)