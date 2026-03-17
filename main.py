# importing libraries

import sounddevice as sd # for accessing mic
import wavio as wv # to convert NumPy array into WAV
import numpy as np # for managing array 

freq = 44100      # sample rate
channels = 1      # mono recording
device = sd.default.device[0]  # default input device

print("Press Ctrl+C to stop recording at any time!")

# Buffer to store audio chunks
recorded_frames = []

try:
    # open input stream
    with sd.InputStream(samplerate=freq, channels=channels, dtype='int16', device=device) as stream:
        while True:
            data, _ = stream.read(freq)
            recorded_frames.append(data)
except KeyboardInterrupt:
    print("\nRecording stopped by user!")

# Convert list of chunks to a single NumPy array
recording = np.concatenate(recorded_frames, axis=0)

# save using wavio
wv.write('manual_recording.wav', recording, freq, sampwidth=2)
print("File saved: manual_recording.wav")

# play back immediately
sd.play(recording, freq)
sd.wait()
print("Playback finished.")