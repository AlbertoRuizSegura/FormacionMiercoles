import openai
import tiktoken
import json

from config import Config

openai.api_base=Config.OPENAI_API_BASE
openai.api_key=Config.OPENAI_API_KEY
openai.api_type=Config.OPENAI_API_TYPE
openai.api_version=Config.OPENAI_API_VERSION

deployment = Config.OPENAI_CHAT_DEPLOYMENT

archivo = open('Correo.txt','r',encoding="utf-8")
contenido = archivo.read()

def prompt_context(context):
    return f"""
        Eres un asistente encargado de extraer información de un correo electrónico.
        Para ello, extraes una serie de información y la almacenas en formato Json.
        La información a extraer es la siguiente 'Usuario que envía el email', 'Usuario que recibe el email','Hora de envío','Subject' y un array de 'Lista de tareas'
        A continuación, se incluye el correo a analizar: ````{context}''''
        """


conversation = [{"role":"user","content":prompt_context(contenido)}]
response = openai.ChatCompletion.create(
    engine=deployment,
    messages = conversation,
    temperature=0.7,
    max_tokens=150,
    stop=None
)

print(response['choices'][0]['message']['content'])     #Respuesta del OpenAI

file_name = "DatosCorreo"
with open(file_name, 'w') as json_file:
    json.dump(response['choices'][0]['message']['content'], json_file)

