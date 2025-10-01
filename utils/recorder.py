import sounddevice as sd
from scipy.io.wavfile import write

def record_voice(file_path, duration=3, fs=44100):
    print("🎙️ Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(file_path, fs, audio)
    print("✅ Recording saved.")
