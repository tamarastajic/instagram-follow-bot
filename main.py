from InstaFollower import InstaFollowerBot

# Input Proper Values
INSTAGRAM_USERNAME = YOUR_INSTAGRAM_USERNAME
INSTAGRAM_PASSWORD = YOUR_INSTAGRAM_PASSWORD

INSTAGRAM_ACCOUNT_REPLICATE = INSTAGRAM_USERNAME_FOLLOWERS_TO_FOLLOW


bot = InstaFollowerBot()
bot.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
bot.follow(INSTAGRAM_ACCOUNT_REPLICATE)
