import os, sys, time
from rich import print
from time import sleep

def run():
    print("[turquoise2][INFO][/turquoise2][light_green] DOse .NET botnet selecting PROTOCOL method[/light_green]")
    sleep(1)
    print("[turquoise2][INFO][/turquoise2][light_green] METHOD SELECTED[/light_green]")
    sleep(1)
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(100):
       time.sleep(0.1)
       sys.stdout.write("\rloading method.... " + animation[i % len(animation)])
       sys.stdout.flush()
    print()
