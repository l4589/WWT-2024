from openai import OpenAI



def customTranscript(vData):
    client = OpenAI()

    print('custom transcript', vData)
    if vData["SimpleVocab"]:
        sVocab = 'and simple words,'
    else: 
        sVocab = ' '
    if vData['bulletpoints']:
        bPoints = 'in bullet points'
    else:
        bPoints = ' '
        
    gradeLevel = vData['gradeLevel']

    with open("AItext.txt", "r") as f:
        text = f.read()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"You are a {gradeLevel} grade student studying, who returns data in HTML format."},
        {"role": "user", "content": f"Summarize this lecture {bPoints} {sVocab} as HTML code: {text}"}
    ]
    )
    print(completion.choices[0].message)

    aitext=completion.choices[0].message.content

    return aitext
