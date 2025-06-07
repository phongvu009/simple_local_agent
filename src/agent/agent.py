from openai import OpenAI


class Agent:
    """Create an agent"""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        model_name: str,
        system_prompt: str | None = "",
    ):
        # create instance openai
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        # messages history
        self.messages = []
        self.model_name = model_name

        self.system_prompt = system_prompt
        # system prompt option
        if self.system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})

    def __call__(self, message):
        """ """
        # add user message to history chat
        user_msg = {"role": "user", "content": message}
        self.messages.append(user_msg)
        result = self._execute()
        # add response to history chat
        assistant_msg = {"role": "assistant", "content": result}
        self.messages.append(assistant_msg)
        return result

    def _execute(self):
        # send whole message history
        response = self.client.chat.completions.create(
            model=self.model_name, messages=self.messages, top_p=0.1
        )

        # Setting temperature to have consistant answer
        # response = self.client.beta.chat.completions.parse(
        #     temperature=0,
        # )
        result = response.choices[0].message.content
        return result
