import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Clinic assistant"
telegram_bot_token = os.getenv("telegram_token")
llm_key_token = os.getenv("token_llm")

if __name__ == "__main__":
    print(telegram_bot_token)
    print(llm_key_token)
    print(APP_NAME)