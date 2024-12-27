fileopen = open("E:\\SEM6\\project\\Raven\\data\\Api.txt","r")
API = fileopen.read()
fileopen.close()



import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv()

messages =[{"role": "system","content":"computer expert"}]

completion = openai.Completion()

def AIreply(question,chat_log = None):

    filelog = open("E:\\SEM6\\project\\Raven\\DataBase\\chatlog.txt","r")
    chat_log_templet = filelog.read()
    filelog.close()

    if chat_log is None:

        chat_log = chat_log_templet

    prompt = f'{chat_log}You : {question}\nRaven : '

    messages.append({"role":"user","content":question})

    response = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages=messages  
    )
    answer = response["choices"][0]["message"]["content"]

    messages.append({"role":"assistant","content":answer})

    chat_log_templet_update = chat_log_templet + f"\nYou : {question} \nRaven : {answer}"

    filelog = open("E:\\SEM6\\project\\Raven\\DataBase\\chatlog.txt","w")
    filelog.write(chat_log_templet_update)
    filelog.close()

    return answer


# kk = input("enter : ")

# print(AIreply(kk))




