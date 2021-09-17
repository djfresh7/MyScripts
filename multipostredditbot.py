# Post Items
t = "Video Name Here"
u = "URL Here"

# Subreddits
subreddits = [
  "Advertise", "AdvertiseEverything", "AdvertiseYourVideos", "advertiseyoutube", "GetMoreViewsYT", "SubscribeToMe", "LetsPlayCritiques", "newreddits", "NewYouTubeChannels", "promote", "Promote_Your_Channel", "PromoteGamingVideos", "promoteyoutube", "PromoteYoutubeGaming", "SelfPromotionYouTube", "shamelessplug", "smallchannelmovement", "SmallYoutubePromoter", "SmallYoutubers", "SmallYoutubersBoost", "Streamers", "SmallYTChannels", "videos", "Sub4Sub", "Sub4subGrowth", "SubForSub", "SubForSub_", "subreddit", "SupportTheSubs", "YoutubeChannelSharing", "YouTubeGamers", "YouTubeHD", "YouTubePromoter", "youtubepromotion", "YoutubePromotionn", "YouTubeSubscribeBoost", "YouTubeVideoShare", "Youtubeviews"
]

for subreddit in subreddits:
  count += 1
  try:
    reddit.subreddit(subreddit).submit(title=t, url=l, send_replies=True)
    print("Successfully posted to:", subreddit, "Posted to", count, "of", len(subreddits), "subreddits")
  except praw.exceptions.RedditAPIException as exception:
    for subexception in exception.items:
      if subexception.error_type == "RATELIMIT":
        wait = str(subexception)
        if "minute" in wait:
          wait = wait[70:72]
          wait = int(wait) + 1
          print("Need to wait", wait, "minutes.")
        else:
          wait = 1
        print("Waiting for", wait, "minutes...")
        time.sleep(wait)
        reddit.subreddit(subreddit).submit(title=t, url=l, send_replies=True)
        print("Successfully posted to:", subreddit, "Posted to", count, "of", len(subreddits), "subreddits")
      else:
        continue
