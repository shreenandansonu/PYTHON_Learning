import serial
import time
import wave

# === CONFIG ===
PORT = 'COM24'         # Replace with your COM port (e.g., 'COM5' on Windows or '/dev/rfcomm0' on Linux)
BAUDRATE = 115200
DURATION_SECONDS = 10
name=input("Please Enter Name:- ")
soundtype=input("Please enter 1 for heart and 2 for lungs:- ")
types="1"
if(soundtype=="1"):
    types="_Heart_"
elif soundtype=="2":
    types="_Lungs_"
OUTPUT_FILENAME = name+types+".wav"
SAMPLE_RATE = 1000
CHANNELS = 1
SAMPLE_WIDTH = 1  # 1 byte = 8-bit audio

# === OPEN SERIAL PORT ===
ser = serial.Serial(PORT, BAUDRATE, timeout=1)
print(f"Connected to {PORT} at {BAUDRATE} baud")

# === CAPTURE AUDIO ===0
audio_data = bytearray()
start_time = time.time()

print(f"Recording for {DURATION_SECONDS} seconds...")

while time.time() - start_time < DURATION_SECONDS:
    if ser.in_waiting:
        chunk = ser.read(ser.in_waiting)
        audio_data.extend(chunk)

ser.close()
print(f"Captured {len(audio_data)} bytes")

# === SAVE AS WAV FILE ===
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(audio_data)

print(f"Saved as {OUTPUT_FILENAME}")
