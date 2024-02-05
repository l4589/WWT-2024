from openai import OpenAI
client = OpenAI()

with open("adamsMIT17.txt", "r") as f:
    text = f.read()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a high school student studying"},
    {"role": "user", "content": f"Summarize this lecture: {text}"}
  ]
)

print(completion.choices[0].message)