#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import sx126x
import time

# Initialize LoRa module
node = sx126x.sx126x(
    serial_num="/dev/ttyS0",
    freq=868,         # Set frequency (868 MHz or 433 MHz)
    addr=0,           # Node address
    power=22,         # Transmit power (10/13/17/22 dBm)
    rssi=False,
    air_speed=2400,
    relay=False
)

def send_message(addr, freq, message):
    """Send message to given node address"""
    offset_freq = int(freq) - (850 if int(freq) > 850 else 410)
    data = (
        bytes([int(addr) >> 8]) +
        bytes([int(addr) & 0xff]) +
        bytes([offset_freq]) +
        bytes([node.addr >> 8]) +
        bytes([node.addr & 0xff]) +
        bytes([node.offset_freq]) +
        message.encode()
    )
    node.send(data)
    print(f"✅ Sent to {addr} at {freq} MHz → {message}")

if __name__ == "__main__":
    while True:
        try:
            # Example input: 0,868,Hello World
            raw = input("Enter as addr,freq,message (Ex: 0,868,Hello): ")
            parts = raw.split(",")
            if len(parts) < 3:
                print("❌ Invalid format. Try again.")
                continue
            send_message(parts[0], parts[1], ",".join(parts[2:]))
        except KeyboardInterrupt:
            print("\nExiting Sender...")
            break
