import argparse

from serial import Serial

from spc import Spc
from list_action import ListAction
from uart import Uart

parser = argparse.ArgumentParser(description='Program to upload a SNES SPC music file to the original sound module via Arduino over serial')
parser.add_argument('serial_port', help='Serial port to use. Usually COM1 on Windows or /dev/ttyUSB0 on Linux')
parser.add_argument('spc_file', help='Path to the SPC sound file')
parser.add_argument("-l", "--list", help="Print available serial ports", action=ListAction)
args = parser.parse_args()

with open(args.spc_file, 'rb') as f:
    spc = Spc(f)
    with Serial(args.serial_port, timeout=5) as serial:
        print('opened port {0}'.format(serial.name))
        Uart.writeRam(serial, spc)
