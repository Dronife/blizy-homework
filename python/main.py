import os
import sys
import command_manager
from dotenv import load_dotenv
from src.database import db

load_dotenv()

def main():
    command_manager.manage(sys.argv)

if __name__ == "__main__":
    main()

