# Post items
t = "Video Name Here"
u = "URL Here"

# Subreddits
subreddits = [
  "Advertise", "AdvertiseEverything", "AdvertiseYourVideos", "advertiseyoutube", "GetMoreViewsYT", "SubscribeToMe", "LetsPlayCritiques", "newreddits", "NewYouTubeChannels", "promote", "Promote_Your_Channel", "PromoteGamingVideos", "promoteyoutube", "PromoteYoutubeGaming", "SelfPromotionYouTube", "shamelessplug", "smallchannelmovement", "SmallYoutubePromoter", "SmallYoutubers", "SmallYoutubersBoost", "Streamers", "SmallYTChannels", "videos", "Sub4Sub", "Sub4subGrowth", "SubForSub", "SubForSub_", "subreddit", "SupportTheSubs", "YoutubeChannelSharing", "YouTubeGamers", "YouTubeHD", "YouTubePromoter", "youtubepromotion", "YoutubePromotionn", "YouTubeSubscribeBoost", "YouTubeVideoShare", "Youtubeviews"
]

# Posting to all of the above subs
count = 0
for subreddit in subreddits:
  count+=1
  try:
    reddit.subreddit(subreddit).submit(title=t, url=u, send_replies=True)
    print("Successfully posted to: ", subreddit, "Posted to", count, "of", len(subreddits), "subreddits")
  except praw.exceptions.RedditAPIException as exception:
    for subexception in exception.items:
      if subexception.error_type == "RATELIMIT":
        wait = str(subexception).replace("RATELIMIT: 'Looks like you've been doing that a lot. Take a break for ", "")
        if "minute" in wait:
          wait = wait[:70]
          wait = int(wait) + 1
          print("Need to wait" + wait)
        else:
          wait = 1
        
        print("Waiting for", wait, "minutes")
        time.sleep(wait*60)
        reddit.subreddit(subreddit).submit(title=t, url=u, send_replies=True)
        print("Successfully posted to", subreddit)
        
      else:
        break