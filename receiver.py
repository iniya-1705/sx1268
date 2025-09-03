#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
from LoRaRF import SX126x

# ---------------- GPIO FIX ----------------
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# ---------------- LoRa SETUP ----------------
lora = SX126x()
lora.begin()
lora.setFrequency(433000000)    # Must match TX
lora.setTxPower(22)
lora.setLoRaModulation(7, 5, 125000)
lora.setLoRaPacket(8, True, 255, False, True)

print("LoRa RX started...")

while True:
    if lora.available():   # ✅ packet is ready
        raw_bytes = []
        while lora.available():   # ✅ read until buffer is empty
            raw_bytes.append(lora.read())
        msg = "".join(chr(b) for b in raw_bytes)
        print("Received:", msg, "| RSSI:", lora.packetRssi())
    time.sleep(0.1)
