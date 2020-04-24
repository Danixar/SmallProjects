# Evangellos Wiegers
# Note: be sure to have pyqrcode, pypng, and qrtools installed

#script for creating and reading QR codes

import pyqrcode
import qrtools
from qrtools.qrtools import QR

def create(name, info):
    '''
    Create a QR code
    :param name: name of img file to create (not including .png)
    :param info: what we want the QR code to represent
    :return: N/A
    '''
    code = pyqrcode.create(info)
    code.png(name + ".png", scale=8)

def read(name):
    '''
    Read a QR code .png file
    :param name: name of file w/out .png
    :return: the info/data of the QR code
    '''
    code = QR()
    code.decode(name + ".png")
    return code.data

#main method for testing
if __name__ == '__main__':
    name = input("Enter a name for the image: ")
    if ".png" in name:
        name.replace(".png", "")
    info = input("Enter what you want turned into QR code: ")
    create(name, info)
    print(read(name))