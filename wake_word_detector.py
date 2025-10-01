import pvporcupine
import pyaudio
import struct
import os
from dotenv import load_dotenv


load_dotenv()
access_key = os.getenv("PV_ACCESS_KEY")

def start_wake_word_listener(callback):
    
    custom_keyword_path = "wake_words/custom_jarvis.ppn"  

    if not os.path.exists(custom_keyword_path):
        raise FileNotFoundError(f"Custom wake word file not found at {custom_keyword_path}")

    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[custom_keyword_path]
    )

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length,
    )

    print("🎧 Say your phrase...")

    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)
            if result >= 0:
                print("✅ Wake word detected!")
                callback()

    except KeyboardInterrupt:
        print("🛑 Wake word listener stopped.")

    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        pa.terminate()
        porcupine.delete()
