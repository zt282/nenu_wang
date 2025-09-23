#deepseek的key：sk-9244fc668339462dbad81bf474be105b
import openai

# 获取对话回复
def get_chat_response(prompt, memory, openai_api_key):
    client = openai.OpenAI(api_key=openai_api_key, base_url="https://api.deepseek.com")

    memory.append({'role': 'user', 'content': prompt})

    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=memory,
    )
    return completion.choices[0].message.content

def main():
    # 你需要在这里填入你的 deepseek API key
    openai_api_key = input("请输入你的 deepseek API key：").strip()

    # 初始化记忆
    memory = [{'role': 'system', 'content': '你是一个根据一个话题就可以生成视频的脚本的助手'}]

    print("你好，我是你的 deepseek-chat 通用聊天模型, 请问有什么可以帮到你的？")

    while True:
        prompt = input("\n你: ")
        if prompt.lower() in ["exit", "quit", "退出", "bye"]:
            print("对话结束，再见！")
            break

        response = get_chat_response(prompt, memory, openai_api_key)
        print("AI:", response)

if __name__ == "__main__":
    main()

