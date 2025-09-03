#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sx126x
import time

# Initialize LoRa module
node = sx126x.sx126x(
    serial_num="/dev/ttyS0",
    freq=868,         # Must match sender frequency
    addr=0,           # Node address
    power=22,
    rssi=True,        # Show signal strength
    air_speed=2400,
    relay=False
)

print("📡 Receiver started... Listening for messages at 868 MHz")
try:
    while True:
        node.receive()   # Continuously listen
        time.sleep(0.1)  # Small delay
except KeyboardInterrupt:
    print("\nExiting Receiver...")
