# OS version
import os
os_version = os.getenv('OS')
print(os_version)

# Read environment variable from file 
from dotenv import load_dotenv
load_dotenv()
database = os.getenv('PASSWORD')
print(database)

