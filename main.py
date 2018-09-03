from constants import Constants
import serial
from serial import SerialException
from serial import SerialTimeoutException
import sys
import glob
import time

com = None
list_ports = []


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


if __name__ == "__main__":
    scan_port()
    if len(list_ports) == 0:
        print("There are no COM port to connect on this computer/device! Please connect target device into device")
    else:
        while True:

            time.sleep(1)
