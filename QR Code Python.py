import pyqrcode
import png
from  pyqrcode import QRCode

s = "Mr Programmer Instagram Link - https://www.instagram.com/mr_programmer_1/"

url = pyqrcode.create(s)


url.png('myqr.png',scale = 6,)