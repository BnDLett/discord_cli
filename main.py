import discord_user, cli_utils, threading, time, sys, colorama

global CHANNEL
UUID     = input("Please enter your UUID:\n> ")
USER     = discord_user.user(UUID)
UUID     = "" # Clearing variable for security purposes
CHANNEL  = input("Please enter in a channel ID:\n> ")
LIMIT    = input("Please enter a starting limit:\n> ")

cli_utils.attempt_clear()

global messages
global messages_str
messages_str  = ""
messages_raw  = USER.get_messages(CHANNEL, int(LIMIT))
messages      = []
messages_raw.reverse()

for message in messages_raw:
  messages.append(f"{colorama.Fore.BLUE}{message['author']['username']}: {colorama.Fore.RESET}{message['content']}\n")


def iterate_messages():
  cli_utils.attempt_clear()
  
  global messages
  global messages_str

  messages_str = "".join(messages)
  print(messages_str)
  
  # for message in messages:
  #   print(f"{colorama.Fore.BLUE}{message['author']['username']}: {colorama.Fore.RESET}{message['content']}")

def handle_user_input(USER: discord_user.user):
  print(f"\n{colorama.Back.YELLOW}Warning: When a new message is sent while you're typing a message, then you'll no longer have a message preview of what you've already typed.{colorama.Back.RESET}\n")
  global CHANNEL
  while True:
    user_input = input()
    if user_input.startswith("/channel"):
      content: str = message["content"]
      CHANNEL = content.removeprefix("/channel ")
      continue
    
    USER.send_message(CHANNEL, user_input)

def user_input_flag():
  sys.stdout.write("> ")
  sys.stdout.flush()

iterate_messages()

thread = threading.Thread(target=handle_user_input, args=(USER,))
thread.start()

user_input_flag()

while True:
  time.sleep(0.05) # Reduces CPU stress
  
  message = USER.get_messages(CHANNEL, 1)[0]
  if messages_raw[-1]["id"] == message["id"]:
    continue
  
  data_str = (f"{colorama.Fore.BLUE}{message['author']['username']}: {colorama.Fore.RESET}{message['content']}\n")

  messages_str += data_str
  messages.append(data_str)
  messages_raw.append(message)
  
  iterate_messages()

  user_input_flag()
