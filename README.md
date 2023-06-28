# AI_SalesGuru
autonomous AI agent with langchain for sales chat.



## MEMO

### SalesGPTの例
```
# エージェントの初期化
sales_agent.seed_agent()

# 会話ステージの判定
sales_agent.determine_conversation_stage() # optional for demonstration, built into the prompt

# ユーザー入力を受ける
user_input = input('Your response: ') # Yea, sure
sales_agent.human_step(user_input)


# エージェントの発話
sales_agent.determine_conversation_stage() # optional for demonstration, built into the prompt
sales_agent.step()

```
