import openai
import tiktoken

from config import Config

openai.api_base=Config.OPENAI_API_BASE
openai.api_key=Config.OPENAI_API_KEY
openai.api_type=Config.OPENAI_API_TYPE
openai.api_version=Config.OPENAI_API_VERSION

deployment = Config.OPENAI_CHAT_DEPLOYMENT

archivo = open('data.txt','r',encoding="utf-8")
contenido = archivo.read()

print("Introduce tu pregunta")
InputText = input()

conversation = [{"role":"user","content":InputText + ":" + contenido}]

response = openai.ChatCompletion.create(
    engine=deployment,
    messages = conversation,
    temperature=0.7,
    max_tokens=150,
    stop=None
)

print("Chat respuesta:" + response['choices'][0]['message']['content'])     #Respuesta del OpenAI

