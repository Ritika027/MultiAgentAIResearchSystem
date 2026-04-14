# # from langchain.agents import create_agent
# from langchain.agents import create_react_agent
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from tools import web_search , scrape_url
# from dotenv import load_dotenv

# load_dotenv()

# #model setup
# llm = ChatOpenAI(model = "gpt-4o-mini",temperature=0)

# #1st agent
# def build_search_agent():
#     return create_agent(
#         model = llm,
#         tools = [web_search]
#     )

# #2nd agent

# def build_reader_agent():
#     return create_agent(
#         model = llm,
#         tools = [scrape_url]
#     )

# #create chains
# #writer chain LCEL pipeline

# writer_prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
#     ("human", """Write a detailed research report on the topic below.

# Topic: {topic}

# Research Gathered:
# {research}

# Structure the report as:
# - Introduction
# - Key Findings (minimum 3 well-explained points)
# - Conclusion
# - Sources (list all URLs found in the research)

# Be detailed, factual and professional."""),
# ])

# writer_chain = writer_prompt | llm | StrOutputParser()


# #critic chain
# critic_prompt = ChatPromptTemplate.from_messages([
#      ("system", "You are a sharp and constructive research critic. Be honest and specific."),
#     ("human", """Review the research report below and evaluate it strictly.

# Report:
# {report}

# Respond in this exact format:

# Score: X/10

# Strengths:
# - ...
# - ...

# Areas to Improve:
# - ...
# - ...

# One line verdict:
# ..."""),
# ])

# critic_chain = critic_prompt | llm | StrOutputParser()

# 

from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ------------------ MODEL SETUP ------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ------------------ REACT PROMPT ------------------
from langchain.prompts import PromptTemplate

react_prompt = PromptTemplate.from_template("""
You are an intelligent AI assistant.

You have access to the following tools:
{tools}

Use the following format:

Question: {input}
Thought: think step by step
Action: one of [{tool_names}]
Action Input: input to the tool
Observation: result of the tool
... (repeat Thought/Action/Observation if needed)
Final Answer: give final answer to user

{agent_scratchpad}
""")

# ------------------ SEARCH AGENT ------------------
def build_search_agent():
    agent = create_react_agent(
        llm=llm,
        tools=[web_search],
        prompt=react_prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=[web_search],
        verbose=True
    )

# ------------------ READER AGENT ------------------
def build_reader_agent():
    agent = create_react_agent(
        llm=llm,
        tools=[scrape_url],
        prompt=react_prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=[scrape_url],
        verbose=True
    )

# ------------------ WRITER CHAIN ------------------
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# ------------------ CRITIC CHAIN ------------------
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()