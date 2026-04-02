import string
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# fonction for ask the ai about the real msg
def get_ai_suggestion(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"Below are 25 Caesar cipher decryptions of the same message, each with a different key. Identify which one is readable/meaningful and return ONLY that key number and the decoded message, nothing else.\n\n{text}"
            }
            
        ]
    )
    return response.choices[0].message.content

with open("message.txt","r") as f:
    r=f.read()

with open("message_chifre.txt","w") as g:
    for i in range(1,26):
        g.write(f"key-------{i}\n")
        l = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for j in r.upper():
            if j in string.digits or j in string.punctuation or j==" " or j == "\n":
                g.write(j)
            else:
                g.write(l[(l.index(j)+i)%26])
        g.write("\n")

with open("message_chifre.txt","r") as m :
    text=m.read()
    print(get_ai_suggestion(text))
    