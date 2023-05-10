import os, sys
import requests
import modules
import socket

from geo_iplookup import hackertarget_lookup
from rich import print
from rich.console import Console
from rich.table import Table
from time import sleep

import modules.flood as fl
import modules.udpflood as UDP
import modules.httpflood as HTTP

os.system('clear')
print("""[spring_green2]

▓█████▄  ▒█████    ██████ ▓█████ 
▒██▀ ██▌▒██▒  ██▒▒██    ▒ ▓█   ▀ 
░██   █▌▒██░  ██▒░ ▓██▄   ▒███   
░▓█▄   ▌▒██   ██░  ▒   ██▒▒▓█  ▄  .NET
░▒████▓ ░ ████▓▒░▒██████▒▒░▒████▒
 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░
 ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░     ░   
   ░        ░ ░        ░     ░  ░
 ░
[/spring_green2]""")
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(90):
    sleep(0.1)
    sys.stdout.write("\rloading DOse.... " + animation[i % len(animation)])
    sys.stdout.flush()
    

print("\n[bold medium_spring_green]DONE😈 ready to DDos[/bold medium_spring_green]")
print("[bold medium_spring_green]type (help) for more options[/bold medium_spring_green]")

def menu():
    try:
        flood = input("[DOse]: ").strip()
    except:
        print("")
        print("[blue1]aww, leaving so soon :( [blue1]")
        sleep(0.1)
        print("[blue1]ok, bye bye[/blue1]")
        sys.exit()

    if flood=="help":
       table = Table(title="[italic magenta1]DOse - the best BOTnet👾[/italic magenta1]")
       table.add_column("DOse modes", justify="right", style="magenta")
       table.add_column("DOse options", justify="right", style="magenta")

       table.add_row("UDP HTTP", "set mode")
       table.add_row("IP - example(8.8.8.8)", "set ip")
       table.add_row("PORT - default(80)", "set port")
       table.add_row("TIME - default(60)", "set time")
       table.add_row("IPLOOKUP - example(8.8.8.8)", "investigate")
       table.add_row("Check host connection", "check host")
       table.add_row("LIST SETTINGS - example(ip, port, mode, time)", "ls")
       table.add_row("DDOS", "run")
       table.add_row("clear screen", "clear")
       console = Console()
       console.print(table)
       menu()

#DOse set commands
    elif flood=="set ip":
         global IP
         IP = str(input("[DOse]ip: ")).strip()
         print("IP - ["+IP+"]")
         menu()

    elif flood=="set mode":
         global MODE
         MODE = str(input("[DOse]mode: ")).strip()

         if MODE=="UDP":
            print("MODE - [UDP]")
            menu()
         elif MODE=="HTTP":
              print("MODE - [HTTP]")
              menu()
         else:
             print("[orange3] "+MODE+" is not a option (UDP) or (HTTP)[/orange3]")
             menu()

    elif flood=="set port":
         global PORT
         PORT = str(input("[DOse]port: ")).strip()
         print("PORT - ["+PORT+"]")
         menu()

    elif flood=="set time":
         global TIME
         TIME = str(input("[DOse]time: ")).strip()
         print("TIME - ["+TIME+"]")
         menu()

    elif flood=="ls":
         try:
             table = Table(title="[italic magenta1]SETTINGS👾[/italic magenta1]")
             table.add_column("DOse Options", justify="left", style="magenta")
             table.add_column("DOse settings", justify="left", style="magenta")

             table.add_row("MODE SET", MODE)
             table.add_row("IP SET", IP)
             table.add_row("PORT SET", PORT)
             table.add_row("TIME SET", TIME)
             console = Console()
             console.print(table)
             sleep(1)
             print("[turquoise2][INFO] successful, now you can type run[/turquoise2]")

         except:
             print("[turquoise2][ERROR] not all options are defind yet, you need to input all options[/turquoise2]")
             menu()
         menu()

    elif flood=="":
         menu()

    elif flood=="investigate":
         try:
             hackertarget_lookup()
         except:
             print("[turquoise2][ERROR] there was a problem getting your data (10,000 requests)per hour[/turquoise2]")
         menu()

#run but if mode = udp then redirect to udpflood.py but if mode = http then redirect to httpflood.py
    elif flood=="run":
#         try:
         print("[turquoise2][INFO][/turquoise2][light_green] all options defined MODE-SET-TO="+MODE+" HOST="+IP+" PORT="+PORT+" TIME="+TIME+"[/light_green]")
         sleep(1)
         if MODE=="UDP":
            pwd = os.getcwd()
            print("[turquoise2][INFO][/turquoise2][light_green] importing IP - IP="+IP+"...[/light_green]")
            host = open(pwd+"/modules/ip", "w")
            host.write(IP)
            host.close()
            sleep(1)
            print("[turquoise2][INFO][/turquoise2][light_green] importing PORT - PORT="+PORT+"...[/light_green]")
            port = open(pwd+"/modules/port", "w")
            port.write(PORT)
            port.close()
            sleep(1)
            print("[turquoise2][INFO][/turquoise2][light_green] importing TIME - TIME="+TIME+"...[/light_green]")
            timer = open(pwd+"/modules/time", "w")
            timer.write(TIME)
            timer.close()
            sleep(1)
            fl.run()

            UDP.udp()
         elif MODE=="HTTP":
              HTTP.http()
#         except:
#             print("[turquoise2][ERROR] no method selected (define all options)[/turquoise2]")
#             menu()
         menu()

#clear screen but print banner
    elif flood=="clear":
         os.system('clear')
         print("""[spring_green2]

▓█████▄  ▒█████    ██████ ▓█████
▒██▀ ██▌▒██▒  ██▒▒██    ▒ ▓█   ▀
░██   █▌▒██░  ██▒░ ▓██▄   ▒███
░▓█▄   ▌▒██   ██░  ▒   ██▒▒▓█  ▄  .NET
░▒████▓ ░ ████▓▒░▒██████▒▒░▒████▒
 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░
 ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░     ░
   ░        ░ ░        ░     ░  ░
 ░
         [/spring_green2]""")
         menu()

    elif flood=="check host":
         try:
             print(IP, PORT)
         except:
             print("[turquoise2][ERROR] you have not definded the ip and port option yet[/turquoise2]")
             menu()
         try:
             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             s.connect(IP, PORT)
             print("[turquoise2][INFO] host connection is good[/turquoise2]")
             s.close()
         except:
             print("[turquoise2][INFO] host connection might be down[/turquoise2]")
             menu()

    else:
        print("[orange3] idk what "+flood+" means and i dont think its a command i have[/orange3]")
        menu()

menu()
