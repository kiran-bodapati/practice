#Remove all files in a directory that were created in last 24 hours/a day
import os
import time

current_time_since_epoch=time.time()
print(f"current time is {current_time_since_epoch}")
seconds_in_a_day=24*60*60



#print(os.path.getctime("/home/bsl025/Downloads/Downloads/my_Practice/os_module/folder_to_practice_removing_files_using_os"))
for file in os.listdir("/home/bsl025/Downloads/Downloads/my_Practice/os_module/folder_to_practice_removing_files_using_os"):
      seconds_since_epoch_in_float=(os.path.getmtime(file))
      if current_time_since_epoch-seconds_since_epoch_in_float<=seconds_in_a_day:
         os.remove(f"/home/bsl025/Downloads/Downloads/my_Practice/os_module/folder_to_practice_removing_files_using_os/{file}")

print(os.listdir("/home/bsl025/Downloads/Downloads/my_Practice/os_module/folder_to_practice_removing_files_using_os"))
#print(time.time())