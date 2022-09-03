import requests
import json
import time
from time import strftime, gmtime
import pyautogui
from dotenv import load_dotenv
from os import getenv

load_dotenv()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler


fig, ax = plt.subplots(num=None, figsize=(16, 9), dpi=80, facecolor='w', edgecolor='k')

ax.set_facecolor("#0B0C0D")#15171A


#to change the border color around the back
fig.patch.set_facecolor('#0B0C0D')
 
# x axis values
x = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
# corresponding y axis values
y = [2,4,1, 3, 6 , 2 ,1 ,8, 4 ,2]
 
# plotting the points
plt.plot(x, y, color='#0642D4')

ax.spines['right'].set_color('#0B0C0D')
ax.spines['top'].set_color('#0B0C0D')
ax.spines['left'].set_color('#8FA3BD')
ax.spines['bottom'].set_color('#8FA3BD')
ax.xaxis.label.set_color('red')
ax.tick_params(axis='x', colors='#8FA3BD')
ax.tick_params(axis='y', colors='#8FA3BD')

mpl.rcParams['lines.linewidth'] = 1
mpl.rcParams['lines.linestyle'] = '--'
    
# function to show the plot
plt.tight_layout()
plt.show()
# plt.savefig('foo.png')