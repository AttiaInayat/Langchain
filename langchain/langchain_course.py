from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROK_API_KEY")
llm = ChatOpenAI(
    model="llama3-8b-8192",  # or llama3-70b-8192
    openai_api_key=api_key,
    openai_api_base="https://api.groq.com/openai/v1",
)
# ---------------------------Chains--------------------------------------------
from langchain.chains import LLMChain,SequentialChain, ConversationalChain
chain1= LLMChain(llm=llm, prompt="",output_key="name")
print(chain1.memory)
chain2= LLMChain(llm=llm, prompt="",output_key="menu_items")

final_chain= SequentialChain(
    chains=[chain1,chain2],
    input_variables=['cuisine'],
    output_variables=['name','menu_items']
)

final_chain({'cuisine':'pakistani'})



# ---------------------------Agents--------------------------------------------

from langchain.agents import load_tools, initialize_agent, AgentType

tools = load_tools(["serpapi", "llm-math", "wikipedia"], llm=llm)
agent = initialize_agent(
    llm=llm, tools=tools, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent.invoke('what is the gdp of pakistan?')

# ---------------------------Memory--------------------------------------------
from langchain.memory import ConversationBufferMemory,ConversationBufferWindowMemory
memory1= ConversationBufferMemory()
memory2=ConversationBufferWindowMemory(k=1)

chain1=LLMChain(llm=llm,prompt="",memory=memory1)
print(chain1.memory.buffer)

convo= ConversationalChain(llm=llm,memory=memory2)
print(convo.prompt.template)