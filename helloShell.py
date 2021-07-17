import subprocess as sp
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def ping():
    res = str(sp.run("ping  www.google.com", shell=True, capture_output=True, text=True))
    #finds numbers between 00 and 9999
    pattern="time=[0-9]{0,9}"
    search = re.findall(pattern, res)
    time = []
    for i in search:
        i = i.replace("time=", "")
        time.append(i)
    return time


for i in range(10):
    res = ping()
    print(res)
