import serial
import struct
import wave
import time

# -------- CONFIGURE --------
SERIAL_PORT = 'COM20'     # Change to your port (e.g., 'COM5' or '/dev/ttyUSB0')
BAUD_RATE = 115200
DURATION_SECONDS = 15     # How long to record (in seconds)
SAMPLING_RATE = 8000     # Match with Arduino's 8kHz
# name=input("Name: ")
OUTPUT_FILENAME = "output.wav"
# ---------------------------

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

frames = []
start_time = time.time()

print(f"Recording {DURATION_SECONDS} seconds of audio...")

while time.time() - start_time < DURATION_SECONDS:
    data = ser.read(2)
    if len(data) == 2:
        value = struct.unpack('>H', data)[0]  # 10-bit ADC value (0–1023)
        # Convert to 8-bit (0–255) for WAV (optional: scale or clip)
        value_8bit = int(value / 1023 * 255)
        frames.append(value_8bit.to_bytes(1, byteorder='little'))

print("Recording complete. Saving WAV...")

# Save to 8-bit mono WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(1)           # Mono
    wf.setsampwidth(1)           # 8-bit
    wf.setframerate(SAMPLING_RATE)
    wf.writeframes(b''.join(frames))

print(f"Saved as {OUTPUT_FILENAME}")