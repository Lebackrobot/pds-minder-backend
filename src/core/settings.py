import os

from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()
        
        self.DB_CONNECTION = os.getenv('DB_CONNECTION')

settings = Settings()