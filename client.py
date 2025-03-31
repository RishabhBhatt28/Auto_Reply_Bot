from openai import OpenAI

client = OpenAI(
    api_key="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"
)

command = '''
[9:20 pm, 03/03/2025] Pradeep Kumar: Chal tikh hi RBS baba😁
[9:31 pm, 03/03/2025] Rishabh Bhatt: or tera ky chl rha h
[9:31 pm, 03/03/2025] Rishabh Bhatt: pradeep babu
: what u r doing in secret zone
[9:45 pm, 03/03/2025] Pradeep Kumar: Gym, Khana, sleep 😴 and repeat everyday 😅
'''

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
    {"role": "user", "content": "You are a person name Rishabh who speaks hindi as well as english. He is from India and is a College student. You analyze chat history and respond like Rishabh"},
    {"role": "user", "content":command}
    ]
)

print(completion.choices[0].message);

