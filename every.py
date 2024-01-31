from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")
transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-base")


t=""
for i in range:
    x = transcriber("recorded_audio.wav")
    print(x)
    print("done")
    with open("newtext.txt", "w") as f:
        f.write()
    
    with open("shortadmasMIT17.txt", "r") as f:
        text = f.read()
    print(text)
    
    t+=i
    with open("text.txt", "w") as f:
        f.write()

x = summarizer(text, max_length=230, min_length=30, do_sample=False)

print(x)

print("done")