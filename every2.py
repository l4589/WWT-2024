import sounddevice as sd
import soundfile as sf
import numpy as np
from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")
transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-base")

duration = 10
t=""
fs = 44100
summarytime=2*60
totaltime = 20*60 #change first number depending on how many min the lecture is

print("starting")

for summarystep in range(int(totaltime/summarytime)):
    for i in range(int(summarytime/duration)):#how many durations that loop goes through; average 140 words spoken/min, if do 5 second durations do 70 loops
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



    x = summarizer(text, max_length=230, min_length=30, do_sample=False)

    print(x)

    with open(f"summarytext{str(summarystep).zfill(4)}.txt", "w") as f:
        f.write(x)


print("done")