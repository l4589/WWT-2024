from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")


with open("shortadmasMIT17.txt", "r") as f:
    text = f.read()
print(text)
 

x = summarizer(text, max_length=230, min_length=30, do_sample=False)

print(x)

print("done")