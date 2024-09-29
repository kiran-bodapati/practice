#check if a particular 'env' variable is present or not

import os
from dotenv import load_dotenv 
load_dotenv()

if not "fake_url" in os.environ.keys():
    print("There is no env variable named 'fake_url' ")
else:
    print(os.environ["fake_url"])
