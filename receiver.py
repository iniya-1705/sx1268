#!/usr/bin/env python3
import time
from LoRaRF import SX126x

# Initialize LoRa
lora = SX126x()

def setup():
    print("LoRa Receiver Init...")
    lora.begin()
    lora.setFrequency(433000000)          # 433 MHz (must match TX)
    lora.setRxGain(0x94, 0xF5)            # Recommended RX gain
    lora.setLoRaModulation(7, 5, 125000)  # Same as TX
    lora.setLoRaPacket(8, True, 255, False, True)

def loop():
    if lora.available():
        length = lora.available()
        msg = ""
        for i in range(length):
            msg += chr(lora.read())
        print("Received:", msg)

    time.sleep(0.5)

if __name__ == "__main__":
    setup()
    while True:
        loop()
