#!/usr/bin/env python3
import time
from LoRaRF import SX126x

lora = SX126x()
lora.begin()
lora.setFrequency(433000000)
lora.setTxPower(22)
lora.setLoRaModulation(7, 5, 125000)
lora.setLoRaPacket(8, True, 255, False, True)

print("LoRa TX started...")

while True:
    msg = "Hello"
    print("Sending:", msg)
    lora.beginPacket()
    for ch in msg:
        lora.write(ord(ch))
    lora.endPacket()
    time.sleep(2)
