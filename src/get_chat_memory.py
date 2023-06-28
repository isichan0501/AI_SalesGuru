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


def get_dynamodb_memory_history(session_id="38"):

    message_history = DynamoDBChatMessageHistory(table_name="SessionTable", session_id=session_id)
    message_history.clear()

    # ai_msg1 = """メアドありがとうございます！ひとみです(o^^o)

    # サイトでもお伝えしましたが、経験人数は1人なんですけど思い切ってカラダの関係で長期で会える人を探しています☆
    # お会いして盛り上がったらゆっくり時間を使ってイチャイチャしたり濃厚なエッチも出来たら嬉しいです♪

    # あとはお会いするときの条件のお話なんですけど、初回はネットでの出会いの相場の2万を預かりたいのですが、お願いできますか？？
    # お金目当てじゃないのでこのお金は2回目以降のホテル代に充てますし、何回か会って預かった2万を使い切ったら、その後のホテル代は対等に折半で構いません◎

    # もし良かったらお会いしましょう！
    # お返事待ってます(o^^o)"""

    # user_msg1 = """メール有難う。マサおじさんです。私の様な高齢者とでもお逢いしていただけるなら、何の問題も有りません。
    # 何処へでもお迎えに上がります。どちらへ伺えば、お会い出来ますでしょうか？"""

    # ai_msg2 = """大丈夫なら良かったです！
    # お互いにたくさん気持ちよくなれるように頑張りますね♪

    # 良かったら早速お会いしたいんですけど、最初はドタキャンとか冷やかしが怖いので私の近場の名古屋駅周辺での待ち合わせでお願いしますm(_ _)m
    # 2回目以降はドタキャンの心配はないので、どの場所でも大丈夫です！

    # ちなみに今日ってお会い出来たりしますか？
    # 難しかったら何日に会えるか教えてください◎"""

    # user_msg2 = """了解しました。名古屋の何処で、待ち合わせしますか？6月の16日の午後14時頃からが、わたしの都ご都合ご都合いかがでしょうか？"""
    # ai_msg3 = "ぜひぜひ！16日の14時に矢場町公園で待ち合わせしましょう！"
    # user_msg3 = "了解しました。よろしくお願いします。"
    # message_history.add_ai_message(ai_msg1)
    # message_history.add_user_message(user_msg1)
    # message_history.add_ai_message(ai_msg2)
    # message_history.add_user_message(user_msg2)
    # message_history.add_ai_message(ai_msg3)
    # message_history.add_user_message(user_msg3)
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

