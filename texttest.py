summarystep=2
with open("summarytext.txt", "w") as f:
    f.write("")

for i in range(summarystep):
    with open(f"summarytext{str(i).zfill(4)}.txt", "r") as f:
        text = f.read()
    
    with open("summarytext.txt", "a") as f:
        f.write(text)