import serial
import struct
import wave
import time

# -------- CONFIGURE --------
SERIAL_PORT = 'COM6'     # Change to your port
BAUD_RATE = 115200
DURATION_SECONDS = 15    # How long to record (seconds)
SAMPLING_RATE = 8000     # 8 kHz sampling rate
# ---------------------------

# Ask user for a name to create dynamic filename
name = input("Enter a name for the recording (no spaces): ").strip()
if not name:
    name = "output"

OUTPUT_FILENAME = f"{name}.wav"

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

frames = []
start_time = time.time()

print(f"Recording {DURATION_SECONDS} seconds of audio...")

while time.time() - start_time < DURATION_SECONDS:
    data = ser.read(2)
    if len(data) == 2:
        value = struct.unpack('>H', data)[0]
        if value > 1023:
            print(f"Warning: ADC value out of range: {value}")

        value_8bit = int(value / 1023 * 255)
        value_8bit = max(0, min(255, value_8bit))
        frames.append(value_8bit.to_bytes(1, byteorder='little'))

print("Recording complete. Saving WAV...")

with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(1)
    wf.setframerate(SAMPLING_RATE)
    wf.writeframes(b''.join(frames))

print(f"Saved as {OUTPUT_FILENAME}")
