import os
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI  # pyright: ignore[reportMissingImports]
from langchain.tools import tool
from google import genai

from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv 

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)


@tool 
def calculator(a: float , b: float) -> str:
    """ This is a useful for performing basic arthamatic calculations """
    print("Tools is being called")
    return f"sum of {a} and {b} is {a+b}" 

@tool
def say_hello(name: str) -> str:
    """ Use for greeeting the user """
    print("Tools is being called")
    return f"Hello {name}, I hope u are doing well today" 

def main():
    model = llm
    tools =[calculator , say_hello]
    agent_executor = create_react_agent(model , tools)

    print("Welcome! I am your AI assistant. Type quit to exit ")
    print("You can ask me to perform claulations or chat with me")

    while True:
        user_inp = input("\n You: ").strip()

        if user_inp == "quit":
            break
        print("\n Assistant: " , end = "")
        for chunk in agent_executor.stream(
            {"messages" : [HumanMessage(content = user_inp)]}
        ): 
            if "agent" in chunk and "messages" in chunk ["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end = "")

        print() 

if __name__ == "__main__":
    main()