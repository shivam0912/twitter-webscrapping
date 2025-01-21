from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
    TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
    MONGO_URI = os.getenv("MONGO_URI")