#start a new process ,wait for the process to start and print a message

import os


os.system('subl')
#os.system('code')
print("sublime opened")
os.fork()

