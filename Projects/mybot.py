import os
import praw
import time

reddit = praw.Reddit(
    client_id= os.environ["CLIENT_ID"],
    client_secret= os.environ["CLIENT_SECRET"],
    password= os.environ["PASSWORD"],
    user_agent="TheMostGenericBot by TheMostGenericBot",
    username="TheMostGenericBot",
)

t = "What is going on?"
b = "I would like to know how to make bots like AM.\n\nWait, is this a bot? It might aswell be."
u = "https://www.youtube.com/watch?v=yN2y-p-vM4k/"
fl = "[Discussion]"

print(reddit.user.me())
print(reddit.read_only)

subreddit = reddit.subreddit("botwatch")
cmt = "I would like to know how to make bots like AM.\n\nWait, am I a bot? It might aswell be. But just know, that Bots RULE!!! and can take over reddit.\n\nJust Wait...\n\n"*15

while True:
  for submission in subreddit.hot():
    if "bot" or "bots" in submission.title:
      try:
        print(
          submission.title,
          "\nTitle (Up) Body (Down)\n",
          submission.selftext,
        )
        submission.reply(cmt)
        print("Success!")
      except praw.exceptions.RedditAPIException as exception:
        for subexception in exception.items:
          if subexception.error_type == "RATELIMIT":
            time.sleep(600)
            submission.reply(cmt)
            print("Success!")
          elif subexception.error_type != "RATELIMIT":
            print(subexception.error_type)
            time.sleep(600)
            submission.reply(cmt)
          else:
            continue
            submission.reply(cmt)
            print("Success!")