import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 读取 .env 文件

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://openrouter.fans/v1"
)


def ask_simple(question: str) -> str:
    """最简问答，不涉及 Function Calling"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": question}],
        temperature=0.1,
    )
    message = response.choices[0].message
    if message.content is None:
        raise ValueError("模型返回内容为空")
    return message.content


if __name__ == "__main__":
    answer = ask_simple("用一句话解释 Python 的 dict 是什么")
    print(answer)
