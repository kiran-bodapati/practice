#get all the running processes

import os
command="ps aux"
with os.popen(command,'r') as output:
    result=output.read()
    print(result)

