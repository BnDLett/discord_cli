def attempt_clear():
  import os, platform
  
  if platform.platform().startswith("Linux"):
    os.system("cls")
  os.system("clear")