import sounddevice as sd
import soundfile as sf
import numpy as np
from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")
transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-base")

duration = 5
t=""
fs = 44100


print("starting")
for i in range(1):#how many durations that loop goes through
    print(i)

   #record the lecture
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    #print('done')
    file_path = "recorded_audio.wav"  # Set the file path to save the recording
    print(f"Saving recording to {file_path}...")
    sf.write(file_path, myrecording, fs)
    print("Recording saved.")

    #gets recorded audio and does the transcription
    x = transcriber("recorded_audio.wav")
    print(x["text"])
   # print("done")

    #puts transcription into a text file
    t+=x["text"]#taking the text from x "the dictionary"
    with open("text.txt", "w") as f:
        f.write(t)
    
    print("done interation")

    #summary
with open("text.txt", "r") as f:
    text = f.read()
print(text)
    


#x = summarizer(text, max_length=230, min_length=30, do_sample=False)

#print(x)
print("done")