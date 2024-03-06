import openai
import tiktoken

from config import Config

openai.api_base=Config.OPENAI_API_BASE
openai.api_key=Config.OPENAI_API_KEY
openai.api_type=Config.OPENAI_API_TYPE
openai.api_version=Config.OPENAI_API_VERSION

deployment = Config.OPENAI_CHAT_DEPLOYMENT

def num_tokens_from_string(string: str, encoding_name: str) -> int:

    encoding = tiktoken.get_encoding(encoding_name)

    num_tokens = len(encoding.encode(string))

    return num_tokens



print("Chat: "+ "Introduce un mensaje")
msg = input()
print("Numero de Tokens Input" + num_tokens_from_string(msg,"cl100k_base"))
while "Stop" not in msg:
    
    conversation = [{"role":"user","content":msg}]

    response = openai.ChatCompletion.create(
        engine=deployment,
        messages = conversation,
        temperature=0.7,
        max_tokens=150,
        stop=None
    )


    #print(response)
    print("Chat respuesta:" + response['choices'][0]['message']['content'])     #Respuesta del OpenAI
    msg = response['choices'][0]['message']['content'] + input()    #Espera al nuevo Input

    print(num_tokens_from_string(msg,"cl100k_base"))    #Muestra el número de Tokens de la respuestas anteriores + Input nuevo
    print(msg)