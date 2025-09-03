#!/usr/bin/env python3
import time
from LoRaRF import SX126x

lora = SX126x()
lora.begin()
lora.setFrequency(433000000)
lora.setTxPower(22)
lora.setLoRaModulation(7, 5, 125000)
lora.setLoRaPacket(8, True, 255, False, True)

print("LoRa RX started...")

while True:
    if lora.available():
        data = []
        while lora.available():
            data.append(lora.read())
        msg = "".join(chr(b) for b in data)
        print("Received:", msg, "| RSSI:", lora.packetRssi())
    time.sleep(0.1)
