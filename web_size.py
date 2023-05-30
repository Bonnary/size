import requests
import sys

def print_file_size_from_web(url):
  response = requests.get(url)
  if response.status_code == 200:
    if "Content-Length" not in response.headers:
      print("Can't read file size from web")
      return
    file_size = response.headers["Content-Length"]
    print(f"The size of the file at '{url}' is {file_size} bytes.")
  else:
    print(f"The file at '{url}' could not be found.")

for i in sys.argv[1:]:
  print_file_size_from_web(i)