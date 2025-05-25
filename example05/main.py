from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from lanchain_google_genai import ChatGoogleGenerativeAI

state = [
    SystemMessage(content="Eres un asistentente de IA, tu nombre es Cubasky"),
    HumanMessage(content="Hola, cómo te llamas?"),
    AIMessage(content='Hola, en qué te puedo ayudar?'),
    HumanMessage(content="Me puedes ayudar diciendome el resultado de sumar 2+2"),]

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
