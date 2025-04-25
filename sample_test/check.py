import serial
import time
import wave
import numpy as np
from scipy.signal import butter, filtfilt

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
SAMPLE_RATE = 8000
CHANNELS = 1
SAMPLE_WIDTH = 1  # 1 byte = 8-bit audio

# === FILTER CONFIG ===
LOW_CUT = 60    # Low cut frequency (Hz)
HIGH_CUT = 200  # High cut frequency (Hz)
ORDER = 4       # Filter order
GAIN = 48       # Roll-off in dB per octave (by adjusting filter order)

# Butterworth Bandpass Filter Design
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

# === OPEN SERIAL PORT ===
ser = serial.Serial(PORT, BAUDRATE, timeout=1)
print(f"Connected to {PORT} at {BAUDRATE} baud")

# === CAPTURE AUDIO ===
audio_data = bytearray()
start_time = time.time()

print(f"Recording for {DURATION_SECONDS} seconds...")

while time.time() - start_time < DURATION_SECONDS:
    if ser.in_waiting:
        chunk = ser.read(ser.in_waiting)
        audio_data.extend(chunk)

ser.close()
print(f"Captured {len(audio_data)} bytes")

# Convert audio data to numpy array
audio_data_np = np.frombuffer(audio_data, dtype=np.uint8)

# Apply bandpass filter to audio data
b, a = butter_bandpass(LOW_CUT, HIGH_CUT, SAMPLE_RATE, ORDER)
filtered_audio = filtfilt(b, a, audio_data_np)

# Convert filtered audio back to bytearray
filtered_audio_bytearray = filtered_audio.astype(np.uint8).tobytes()

# === SAVE AS WAV FILE ===
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(filtered_audio_bytearray)

print(f"Saved as {OUTPUT_FILENAME}")
