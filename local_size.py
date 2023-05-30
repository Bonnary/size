import os
import sys

def print_local_file_size(file_path):
  if os.path.isfile(file_path):
    file_size = os.path.getsize(file_path)
    print(f"The size of '{file_path}' is {file_size} bytes.")
  else :
    print(f"Can't find file '{file_path}'")


for i in sys.argv[1:]:
  print_local_file_size(i)