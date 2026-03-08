# import libraries 

import sounddevice as sd
import wavio as wv

# Show input/output devices
print(sd.query_devices())

# Parameters
freq = 44100
record_duration = 5
channels = 1

# Use default input device
device = sd.default.device[0]

# Record audio
print("Recording...")
recording = sd.rec(
    int(record_duration * freq),
    samplerate=freq,
    channels=channels,
    dtype='int16',
    device=device
)
sd.wait()
print("Recording finished.")

# Save WAV
wv.write('recording_wv.wav', recording, freq, sampwidth=2)
print("File saved: recording_wv.wav")

# Optional: play back immediately
sd.play(recording, freq)
sd.wait()
print("Playback finished.")