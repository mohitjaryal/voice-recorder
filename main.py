# import libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# sampling frequency

freq = 44100

# recording duration
record_duration = 5

# start recoder 
recording = sd.rec(int(record_duration * freq),
                        samplerate=freq, channels=2)

# record audio for given. no of seconds

