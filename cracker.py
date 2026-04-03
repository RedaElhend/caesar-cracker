import string
from groq import Groq
# this i think is to connect to .env 
from dotenv import load_dotenv
import os
import random

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# fonction for ask the ai about the real msg
def get_ai_suggestion(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"Below are 51 Caesar cipher brute-force decryptions of an unknown message. Each block starts with 'key-------N'. Analyze all of them and find the ONE that forms a readable, meaningful sentence in any language. Respond ONLY in this exact format: 'Key: X | Message: ...' — no explanation, no preamble.\n\n{text}"
            }
            
        ]
    )
    return response.choices[0].message.content

def encrypt(message, k):
    print(f"the key used is {k}")
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = ""
    for i in message:
        if i in letters:
            result = result + letters[(letters.index(i) + k) % 52]
        else:
            result = result+i
    print(result)

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

try:
    while True:
        chose=input("1. Crack a message \n2. Decrypt a message \n3. Encrypt a message\n4. Exit \nchose 1 or 2 or 3 or 4 : ")
        # code part tha crack the message
        if int(chose) == 1:
            message=input("Enter the message you want to crack:\n")
            # try evry key 
            with open("encrypted_message.txt","w") as g:
                for i in range(1,52):
                    g.write(f"key-------{i}\n")
                    for j in message:
                        if j in string.digits or j in string.punctuation or j==" " or j == "\n":
                            g.write(j)
                        else:
                            g.write(letters[(letters.index(j)-i)%52])
                    g.write("\n")
            # ask ai to found the real msg 
            with open("encrypted_message.txt","r") as m :
                text=m.read()
                print("--------- AI answer ------------")
                print(get_ai_suggestion(text))
                print("--------- If you did not like the AI answer, you can check encrypted_message.txt for all key versions")
        elif int(chose)==2:
            try:  
                message=input("Enter the message you want to decrypt: \n")
                key=int(input("key= "))
                for j in message:
                    if j in string.digits or j in string.punctuation or j==" " or j == "\n":
                        print(j,end="")
                    else:
                        print(letters[(letters.index(j)-key)%52],end="")
            except  ValueError:
                print("The key chosen is invalid ")
            except Exception:
                print("Sorry, an error occurred")
            finally:
                print("\n")
        elif int(chose)== 3:
            message=input("Enter the message you want to encrypt: \n")
            # I use ensemble bc I forgth how to use random 👍
            key=random.randint(1,52)
            print("--------Encrypted message--------")
            encrypt(message, key)
        elif int(chose)==4:
            break
        else:
            print("Please choose a number from the list")
except Exception as e:
    print(f"Sorry, an error occurred. Please try again.\nError: {e}")
finally:
    print("------------------------------------------------------------")
