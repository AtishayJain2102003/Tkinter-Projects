import sounddevice as sd
import soundfile as sf
from tkinter import *

def voice_rec():
    fs=48000
    duration=int(input("Enter the duration of recording: "))
    myrecording=sd.rec(int(duration*fs),samplerate=fs,channels=2)
    sd.wait()
    return sf.write("my_audio_file.flac",myrecording,fs)

master=tk()
Label(master,text="Voice Recorder: ").grid(row=0,sticky=W,rowspan=5)
b=Button(master,text="start",command=Voice_rec)
b.grid(row=0,cloumn=2,columnspan=2,rowspan=2,padx=5,pady=5)
mainloop()
