from constants import Constants
import serial
from serial import SerialException
from serial import SerialTimeoutException
import sys
import glob
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import Adafruit_Nokia_LCD as Lcd
import Adafruit_GPIO.SPI as SPI
import os

com = None
list_ports = []
font = ImageFont.load_default()
mainMenu = False
left_button_text = "Select"
right_button_text = "Back"

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 4
# DIN = 17
# DC = 23
# RST = 24
# CS = 8

# Hardware SPI usage:
disp = Lcd.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
# disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()


def detect_env():
    if sys.platform.startswith('win'): return Constants.WIN_SYS
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'): return Constants.LINUX_SYS
    elif sys.platform.startswith('darwin'): return Constants.LINUX_SYS


def scan_port():
    global list_ports
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    list_ports = result


def init_port():
    global com
    com = serial.Serial("COM1")
    com.baudrate = 9600
    com.timeout = 1
    com.parity = serial.PARITY_NONE
    com.bytesize = serial.EIGHTBITS
    com.stopbits = serial.STOPBITS_ONE
    com.xonxoff = serial.XOFF
    com.rtscts = 0


def send_command(cmd):
    if com is None:
        init_port()

    if not com.is_open:
        com.open()

    try:
        com.write(cmd)
    except SerialTimeoutException:
        print("Sent command timeout")
    except SerialException:
        print("Error while send packet")


def receive_serial_packet():
    pass


def show_screen():
    pass


def build_nav_button():
    image = Image.new('1', (Lcd.LCDWIDTH, Lcd.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    selectMaxWidth, selectHeight = draw.textsize(left_button_text, font=font)
    backMaxWidth, backHeight = draw.textsize(right_button_text, font=font)


def build_calling_screen():
    pass


def build_main_menu_screen():
    build_nav_button()
    main_dir = os.path.dirname(__file__)

    contacts_menu = ('Contacts', os.path.join(main_dir, './Resources/contacts_icon.png'))
    messages_menu = ('Messages', os.path.join(main_dir, './Resources/messages_icon.png'))
    calls_menu = ('Calls', os.path.join(main_dir, './Resources/call_register_icon.png'))


def build_idle_screen():
    pass


def build_contact_menu_screen():
    build_nav_button()
    add_menu_item = "Add contact"
    view_all_menu_item = "List all"


def build_list_screen(items):
    build_nav_button()
    for item in items:
        print(item)


if __name__ == "__main__":
    scan_port()
    if len(list_ports) == 0:
        print("There are no COM port to connect on this computer/device! Please connect target device into device")
    else:
        while True:
            time.sleep(1)
