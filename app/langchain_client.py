import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain.tools import Tool
from langgraph.prebuilt import create_react_agent
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from .screen_capture_tool import screen_capture_tool
from .image_processor import read_image

load_dotenv()

# Initialize OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI model
model = ChatOpenAI(model="gpt-4", api_key=openai_api_key)

# Define a tool to read the image
def read_screen_image(_=None) -> str:
    file_path = "screenshot.png"
    return read_image(file_path)

# Define the tools, including the screen capture tool
tools = [
    screen_capture_tool(),
    Tool(
        name="read_screen_image",
        func=read_screen_image,
        description="Reads the text content of the captured screen image."
    ),
    Tool(
        name="dummy_tool",
        func=lambda input_text: f"Processed: {input_text}",
        description="A tool that processes input text."
    )
]

# Create an agent with the model and tools
agent_executor = create_react_agent(model, tools)

# Setting up the conversation chain with SQLite memory
connection_string = "sqlite:///sqlite.db"
session_id = "default_session"

chat_message_history = SQLChatMessageHistory(
    session_id=session_id, connection_string=connection_string
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

chain = prompt | ChatOpenAI(api_key=openai_api_key)

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: SQLChatMessageHistory(
        session_id=session_id, connection_string=connection_string
    ),
    input_messages_key="question",
    history_messages_key="history",
)

def get_langchain_response(prompt: str, session_id: str = "default_session") -> str:
    config = {"configurable": {"session_id": session_id}}
    response = chain_with_history.invoke({"question": prompt}, config=config)
    return response.content  # Returning the AI's response message content

async def stream_langchain_response(prompt: str, session_id: str = "default_session"):
    config = {"configurable": {"session_id": session_id}}
    async for chunk in agent_executor.astream_events({"messages": [HumanMessage(content=prompt)]}, config, version="v1"):
        yield chunk["agent"]["messages"][-1]["content"] if "agent" in chunk else chunk["content"]
