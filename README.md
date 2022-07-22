# spam_Discord

a small script about spamming random messages in discord chat channel. Used to level up in the chat channel (bots MEE6, Arcane, ProBot, etc.). use Python

# How to use:

```

pip install -r "requirements.txt"
python spam_Discord.py
```
### Use 2 credentials (authorization and channel ID) to start spamming

# How to find authorization and channelID
  - Open Discord web
  - choose the channel you want to spam
  - F12 -> network -> Fetch/XHR
  - find messages?limit=50
  - Headers -> General -> Request URL : find number channel ID (circled blue is channel ID)
  ![e07f4d83219ce3c2ba8d](https://user-images.githubusercontent.com/77497884/180369522-dc1cb8ee-6b79-4cd6-a514-1b5f0d4683a7.jpg)
  
  - Headers -> General -> Request headers : find authorization (circled blue)
  ![cad4392a5535976bce24](https://user-images.githubusercontent.com/77497884/180369463-a8197c6d-0a82-4aae-bb65-6cc289bfbe22.jpg)

