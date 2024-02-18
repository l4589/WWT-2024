from openai import OpenAI



def customTranscript():
  client = OpenAI()

  with open("AItext.txt", "r") as f:
      text = f.read()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a  student studying"},
      {"role": "user", "content": f"Summarize this lecture: {text}"}
    ]
  )
  #print(completion.choices[0].message)

  aitext=completion.choices[0].message.content

  return aitext
