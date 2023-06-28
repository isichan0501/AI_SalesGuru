from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.utilities import PythonREPL
from getpass import getpass
from langchain.memory.chat_message_histories import DynamoDBChatMessageHistory


from typing import Dict, List, Any, Tuple
from copy import deepcopy
from langchain import LLMChain, PromptTemplate
from langchain.llms import BaseLLM
from pydantic import BaseModel, Field
from langchain.chains.base import Chain
from langchain.chat_models import ChatOpenAI

from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain.memory import ConversationBufferMemory, ReadOnlySharedMemory
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.utilities import GoogleSearchAPIWrapper

# 環境変数
from dotenv import load_dotenv
import os
load_dotenv()


def get_history_db(session_id="38"):
    message_history = DynamoDBChatMessageHistory(table_name="SessionTable", session_id=session_id)
    # message_history.clear()
    # message_history.add_ai_message(ai_msg1)
    # message_history.add_user_message(user_msg1)
    return message_history


def get_japanese_summary_memory(message_history: ConversationBufferMemory = None):
    if not message_history:
        message_history = get_dynamodb_memory_history()
    
    summary_prompt = PromptTemplate(
        input_variables=["summary", "new_lines"],
        template='''
    会話の行を徐々に要約し、前の要約に追加して新しい要約を返してください。

    例：
    現在の要約：
    人間はAIに人工知能についてどう思うか尋ねます。AIは人工知能が善の力だと考えています。
    新しい会話の行：
    人間：なぜあなたは人工知能が善の力だと思いますか？
    AI：人工知能は人間が最大限の潜在能力を発揮するのを助けるからです。
    新しい要約：
    人間はAIに人工知能についてどう思うか尋ねます。AIは人工知能が善の力だと考えており、それは人間が最大限の潜在能力を発揮するのを助けるからです。
    例の終わり

    現在の要約：
    {summary}
    新しい会話の行：
    {new_lines}
    新しい要約：
        ''',
    )
    llm = ChatOpenAI(temperature=0)
    memory = ConversationSummaryBufferMemory(
        memory_key="chat_history",
        human_prefix="User",
        ai_prefix="Agent",
        llm=llm,
        max_token_limit=200,
        return_messages=True,
        chat_memory=message_history,
        prompt=summary_prompt ### <--- ここでプロンプトを上書き
    )

    return memory

def get_summary_chain(memory):
    template = """
    {history}
    Human: {input}
    AI:"""

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=template
    )
    chain = LLMChain(prompt=prompt,memory=memory,llm=ChatOpenAI(temperature=0))
    return chain

