import tkinter as tk
import random
import json
import time
import requests
from urllib import *

url = "https://raw.githubusercontent.com/zacanger/profane-words/master/words.json"
r = requests.get(url)
content = r.json()
window = tk.Tk()
for i in range(0, len(content)):
    content[i] = content[i].replace(" ", "")

count = 0
def gen():
    global count
    width = [50, 20, 12, 55, 12, 13, 42]
    height = [20, 10, 12, 10, 13, 15]
    colors = ["lightblue", "pink", "orange", "yellow", "purple"]
    curseword.config(text = content[random.randint(0, len(content))], \
                    width = width[random.randrange(0, len(width))], \
                    height = height[random.randrange(0, len(height))], \
                    bg = colors[random.randrange(0,len(colors))], \
                    font = ("Comic Sans MS", random.randrange(10,100)))
    count+=1
    counter.config(text = ("Counter", count))
    window.after(500, gen)
    
counter = tk.Label(window, text = "Counter: 0")
button = tk.Button(window, text = "GENERATE CURSEWORD", command = gen)
curseword = tk.Label(window, text = "")
curseword.pack()
button.pack()
counter.pack()

window.mainloop()

