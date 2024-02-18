from openai import OpenAI



def customTranscript(vData):
    client = OpenAI()

    print('custom transcript', vData)

    if vData['bulletpoints']:
        bPoints = 'in bullet points'

    with open("AItext.txt", "r") as f:
        text = f.read()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a student studying, who returns data in HTML format."},
        {"role": "user", "content": f"Summarize this lecture {bPoints} as HTML code: {text}"}
    ]
    )
    print(completion.choices[0].message)

    aitext=completion.choices[0].message.content

    return aitext
