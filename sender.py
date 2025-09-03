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
lora.setFrequency(433000000)    # 433 MHz
lora.setTxPower(22)             # Max TX power
lora.setLoRaModulation(7, 5, 125000)  # SF7, CR 4/5, BW 125kHz
lora.setLoRaPacket(8, True, 255, False, True)

print("LoRa TX started...")

count = 0
while True:
    msg = f"Hello LoRa #{count}"
    print("Sending:", msg)

    # ✅ Correct way to send
    lora.beginPacket()
    lora.write(msg.encode())
    lora.endPacket()

    time.sleep(2)
    count += 1
