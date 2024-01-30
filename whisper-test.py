from transformers import pipeline

transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-base")

x = transcriber("recorded_audio.wav")

print(x)
print("done")

with open("newtext.txt", "w") as f:
    f.write()
