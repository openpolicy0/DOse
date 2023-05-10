import socket
import rich
import random
import requests
import os
import threading

from rich import print
from rich.console import Console
from rich.table import Table
from time import sleep

def udp():
    print("[turquoise2][INFO][/turquoise2][light_pink4] Starting DDOS cooldown every 10SECs - 1.0KB[/light_pink4]")
    ip = open("/home/kali/DOse_net/modules/ip", "r")
    hp = open("/home/kali/DOse_net/modules/port", "r")
    timer = open("/home/kali/DOse_net/modules/time", "r")
    host = ip.read()
    host_port = hp.read()
    time_set = int(timer.read())
    sleep(1)
    for i in range(0, time_set):
       try:
           sleep(1)
           print("[grey58][SENT][/grey58][pale_turquoise1] packet sent - HOST="+host+" port="+host_port+" Bytes="+xx+"[/pale_turquoise1]".format(str(host), int(host_port), xx))
       except:
           s.close()
           sleep(0.1)
           print("[dark_orange3][DOWN🔥][/dark_orange3][pale_turquoise1] IP.address UDP HOST="+host+" host=down[/pale_turquoise1]")

