from openai import OpenAI

base_url = "http://localhost:11434/v1"
client = OpenAI(base_url=base_url, api_key="empty")


def chat():
    # message history
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "what can you do?"},
    ]

    #
    response = client.chat.completions.create(model="llama3.2:3b", messages=messages)

    # answer
    answer = response.choices[0].message.content
    print(f"Agent: {answer}")


def main():
    print("Hello from simple-local-agent!")
    chat()


if __name__ == "__main__":
    main()
