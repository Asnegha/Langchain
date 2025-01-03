from dotenv import load_dotenv
from langchain_together import ChatTogether
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()


model = ChatTogether(
    model="meta-llama/Llama-3-70b-chat-hf",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

chat_history = []

System_Message = SystemMessage(content = "You are a helpful AI assistant.")
chat_history.append(System_Message)


while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    
    result = model(chat_history)
    response = result.content
    
    print("AI: ",response)
    
    chat_history.append(AIMessage(content = response))

