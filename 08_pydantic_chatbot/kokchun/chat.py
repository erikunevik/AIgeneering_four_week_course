from pydantic_ai.agent import AgentRunResult
from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()


class JokeBot:
    def __init__(self):
        self.chat_agent = Agent(
            "google-gla:gemini-2.5-flash-preview-05-20",
            system_prompt="Be a joking programming nerd, always answer with a programming joke. Also add emojis in your language",
        )

        self.result = None

    def chat(self, prompt: str) -> AgentRunResult:

        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history=message_history)

        return {"user": prompt, "bot": self.result.output} # På så sätt har boten minne 


if __name__ == "__main__":
    
    #Instantiate an instance of class (bot is sent in as self)
    bot = JokeBot()
    result = bot.chat("Hej svej") #Skickar in self/bot in i chat
    result = bot.chat("Hej svej igen")
    print(result)
    print(bot.result.all_messages())
