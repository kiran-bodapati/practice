#get the environmnet varibales and values


import os
from dotenv import load_dotenv
load_dotenv()


#os.getenv("database_url")
#print(os.getenv("database_url"))
for key in os.environ.keys():
   print(f'"key":{key}')

for value in os.environ.values():
   print(f'"value:{value}')