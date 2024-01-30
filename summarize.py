from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")


with open("adamsMIT17.txt", "r") as f:
    text = f.read()
print(text)

x = summarizer("text")

print(x)
print("done")