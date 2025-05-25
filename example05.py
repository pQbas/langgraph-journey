'''
En esta vamos a entender más sobre los tipos de mensajes que existen los cuales son:

- SystemMessage : Contiene las instrucciones del modelo LLM
- HummanMessage : Son los mensajes que han sido enviados por el usuario
- AIMessage : Es el objeto con el que responde un modelo de lenguaje

Cual es la diferencia entre ellos? Y cual es su proposito?

Al final despues de entender esto, se va a realizar un ejemplo usando langchain,
que nos va a permitir interactuar con un modelo de lenguaje cómo si fuera un chatbot
'''

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from lanchain_google_genai import ChatGoogleGenerativeAI

import os

state = [
    SystemMessage(content="Eres un asistentente de IA, tu nombre es Cubasky"),
    HumanMessage(content="Hola, cómo te llamas?"),
    AIMessage(content='Hola, en qué te puedo ayudar?'),
    HumanMessage(content="Me puedes ayudar diciendome el resultado de sumar 2+2"),
]

print(state)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

response = model.invoke(state)

print('------------------------------------')
print([response])


## Ejemplon de un chat simple

state = [
    SystemMessage(content="Eres un asistentente de IA, tu nombre es Cubasky")
]


while True:
    user_input = input(">> ")
    state.append(HumanMessage(content=user_input))

    result = model.invoke(state)
    state.append(result)

    print('response:', state[-1].content)
