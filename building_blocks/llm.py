# from langchain_core.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def batch():
#     try: 
#         chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key=os.getenv("GROQ_API_KEY"))

#         system = "You are a helpful assistant."
#         human = "{text}"
#         prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

#         chain = prompt | chat
#         print(chain.invoke({"text": "Explain the importance of low latency LLMs."}))
#     except Exception as e:
#         print(f"An error occured in batch: {e}")

# # Streaming
# def streaming():
#     try:

#         chat = ChatGroq(temperature=0, model_name="llama2-70b-4096",groq_api_key=os.getenv("GROQ_API_KEY"))
#         prompt = ChatPromptTemplate.from_messages([("human", "Write a very long poem about {topic}")])
#         chain = prompt | chat
#         for chunk in chain.stream({"topic": "The Moon"}):
#             print(chunk.content, end="", flush=True)
#     except Exception as e:
#         print(f"An error occured in streaming: {e}")

# # batch()
# streaming()

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")

def batch():
    try: 
        system_message = {"role": "system", "content": "You are a helpful assistant."}
        user_message = {"role": "user", "content": "Explain the importance of low latency LLMs."}

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[system_message, user_message],
            temperature=0
        )

        print(response.choices[0].message["content"])

    except Exception as e:
        print(f"An error occurred in batch: {e}")

def streaming():
    try:
        system_message = {"role": "system", "content": "You are a helpful assistant."}
        user_message = {"role": "user", "content": "Write a very long poem about The Moon"}

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            # messages=[system_message, user_message],
            messages=[system_message, user_message],
            temperature=0,
            stream=True
        )

        # for chunk in response:
        #     if "choices" in chunk:
        #         print(chunk["choices"][0]["delta"]["content"], end="", flush=True)

        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
                
    except Exception as e:
        print(f"An error occurred in streaming: {e}")

# Uncomment to run batch or streaming
# batch()
streaming()