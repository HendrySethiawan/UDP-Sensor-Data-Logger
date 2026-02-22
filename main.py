import socket
import datetime
import pandas as pd
import math
from pynput import keyboard
import sys
import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)

ip, port = '192.168.88.26', 9999
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("waiting for data...")

mux1=0
mux2=0

df = pd.DataFrame(columns=['time', 's1', 's2','s3','s4',
                            's5', 's6','s7','s8'])

check=''
def Stop(key):
    global check
    if key==keyboard.Key.esc:
        check = 'stop'
        return False
listener = keyboard.Listener(on_release=Stop)
listener.start()

while True:
    if check=='stop':
        print('\nProses berhenti')
        break
    data, addr = s.recvfrom(8192)
    time = datetime.datetime.now()
    print(time,data)
    data=data.decode("utf-8").split(',')
    for i in data[:-1]:
        if (float(i)<0 or math.isnan (float(i)) or math.isinf(float(i))):
            continue
    df=pd.concat([df,pd.DataFrame({'time':[time],'s1':[data[0]],'s2':[data[1]],'s3':[data[2]],'s4':[data[3]]
                                    ,'s5':[data[4]],'s6':[data[5]],'s7':[data[6]],'s8':[data[7]]})], ignore_index=True)


print('Menyimpan data...')
df.to_csv(r'C:\Users\hendr\Documents\Kuliah\PKL\Kegiatan\Data\Data 4 Reyhan Jalan Tanpa Pakai Kaos Kaki.csv')
print('Data tersimpan')
    
s.close()
