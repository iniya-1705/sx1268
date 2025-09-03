#!/usr/bin/env python3
import time
from LoRaRF import SX126x

# Initialize LoRa
lora = SX126x()

def setup():
    print("LoRa Transmitter Init...")
    lora.begin()
    lora.setFrequency(433000000)          # 433 MHz
    lora.setTxPower(22)                   # Power in dBm
    lora.setLoRaModulation(7, 5, 125000)  # SF7, CR 4/5, BW 125kHz
    lora.setLoRaPacket(8, True, 255, False, True)  # Preamble, CRC etc.

def loop():
    msg = "Hello from Pi"
    print("Sending:", msg)
    lora.beginPacket()
    for ch in msg:
        lora.write(ord(ch))   # send char by char
    lora.endPacket()
    
    # confirm TX done
    if lora.checkIrq("TX_DONE"):
        print("Packet sent successfully")
    else:
        print("TX not confirmed")

    time.sleep(2)

if __name__ == "__main__":
    setup()
    while True:
        loop()
