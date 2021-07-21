import subprocess as sp
import threading

def pinger():
    sp.run("py pinger.py")

def plotter():
    sp.run("py plotter.py")

threading.Thread(target=pinger).start()
threading.Thread(target=plotter).start()
