import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print('\t [!][ Uranus-UI7 ~ https://github.com/Uranus-UI7 ]')
print(a+'+'*40)
print('\[!]Waiting..')
sleep(1)
print(b+'\n[!]Retrieve data')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!]Add additional files !')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
njkey = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
njkey.write(key)
njkey.close()
sleep(1)
print(a+'[!]Adding...!')
sleep(1)
print(b+'\n[!]Waiting...!')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!]Success!')
print(a+'[!]New Data!')
sleep(2)
print('git clone https://github.com/termux/termux-package')
print('git clone https://github.com/termux/termux-packages')
print('clear')
