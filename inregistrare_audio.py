import pyaudio
import wave
import sounddevice as sd
import keyboard
from time import *

def audio_recording():
    
    print('asd')  
    # numele fisierului
    filename = "recorded.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # format
    FORMAT = pyaudio.paInt16
    # canalul 1 este canalul de microfon
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 120
    # initializare obiectul pyaudio
    p = pyaudio.PyAudio()
    
    # formatarea obeictului
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
        if keyboard.is_pressed('q'):
            break
    
    print("Finished recording.")
    # opresete si inchide streamul
    stream.stop_stream()
    stream.close()
    # sterge obiectul pyaudio si elibereaza memoria
    p.terminate()
    # salveaza audioul
    # deschide fisierul in 'write bytes'
    wf = wave.open(filename, "wb")
    # seteaza canalul folosit in inregistreaza
    wf.setnchannels(channels)
    # seteaza formatul folosit in inregistrare
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # seteaza rata frameurilor
    wf.setframerate(sample_rate)
    # formateza framurile sub forma de biti
    wf.writeframes(b"".join(frames))
    # inchide fisierul
    wf.close()
    
    
