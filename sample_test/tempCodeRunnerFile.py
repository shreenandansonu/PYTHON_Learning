import serial
import wave
import struct

port = 'COM23'  # Change this to your ESP32 Bluetooth COM port
baudrate = 115200
duration = 10  # Record for 10 seconds
sample_rate = 8000

ser = serial.Serial(port, baudrate)
print("Recording...")

samples = []

try:
    for _ in range(sample_rate * duration):
        data = ser.read(2)
        sample = struct.unpack('<h', data)[0]  # 16-bit signed
        samples.append(sample)

finally:
    ser.close()

# Save as WAV file
with wave.open("filtered_audio.wav", 'w') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join([struct.pack('<h', s) for s in samples]))

print("Saved filtered_audio.wav")
