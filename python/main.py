import os
from dotenv import load_dotenv
from src.database import db

load_dotenv()

def main():
    db.get_product()

if __name__ == "__main__":
    main()
