import serial
import time
import wave
import numpy as np
from scipy.signal import butter, filtfilt

# === CONFIG ===
PORT = 'COM23'         # Update this with the correct COM port
BAUDRATE = 115200
DURATION_SECONDS = 10
SAMPLE_RATE = 8000
CHANNELS = 1
SAMPLE_WIDTH = 1  # 8-bit audio (1 byte)

# === USER INPUT ===
name = input("Please Enter Name: ")
soundtype = input("Enter 1 for Heart or 2 for Lungs: ")
if soundtype == "1":
    types = "_Heart_"
elif soundtype == "2":
    types = "_Lungs_"
else:
    print("Invalid input. Defaulting to _Unknown_.")
    types = "_Unknown_"

OUTPUT_FILENAME = name + types + ".wav"

# === FILTER CONFIG ===
LOW_CUT = 60     # Hz
HIGH_CUT = 200   # Hz
ORDER = 4        # Filter order

# === Bandpass Filter Design ===
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

# === Serial Setup ===
try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    print(f"Connected to {PORT} at {BAUDRATE} baud")
except serial.SerialException as e:
    print(f"Failed to connect to {PORT}: {e}")
    exit(1)

# === Capture Audio ===
print(f"Recording for {DURATION_SECONDS} seconds...")
audio_data = bytearray()
start_time = time.time()

while time.time() - start_time < DURATION_SECONDS:
    if ser.in_waiting:
        chunk = ser.read(ser.in_waiting)
        audio_data.extend(chunk)

ser.close()
print(f"Captured {len(audio_data)} bytes")

# === Process Audio ===
if len(audio_data) == 0:
    print("No data captured.")
    exit(1)

# Convert byte data to numpy array
audio_np = np.frombuffer(audio_data, dtype=np.uint8)

# Normalize from 8-bit unsigned (0–255) to -1.0 to 1.0 float for filtering
audio_norm = (audio_np.astype(np.float32) - 128) / 128.0

# Apply Bandpass Filter
b, a = butter_bandpass(LOW_CUT, HIGH_CUT, SAMPLE_RATE, ORDER)
filtered = filtfilt(b, a, audio_norm)

# Rescale back to 8-bit unsigned integers (0–255)
filtered_uint8 = np.clip((filtered * 128) + 128, 0, 255).astype(np.uint8)

# === Save as WAV File ===
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(filtered_uint8.tobytes())

print(f"Saved filtered audio as: {OUTPUT_FILENAME}")
