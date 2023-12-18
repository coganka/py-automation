import sounddevice
from scipy.io.wavfile import write

secs = 5
fps = 44100

recording = sounddevice.rec(frames= secs * fps, samplerate=fps, channels=1)
sounddevice.wait()

write('output.mp3', fps, recording)