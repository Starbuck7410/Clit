# Clit
CLIT - Command Line Interface for Twitter

Uses Python 3, Selenium with Chromedriver (For version 77), Google chrome, and tweepy.


Commands:
Commands are the key to controlling Clit. Some commands require 1 input, which is the command name, and some require more than one (For example the "browser" command). Commands that require more than 1 input recieve the other inputs in a seperate line (So for the "browser" command, you enter "browser", [Enter], and the tweet ID).

Current commands:
exit - Exits Clit
pagedn - Page down, loads the next 5 tweets (next page)
pagedn - Page up, loads the previous 5 tweets (previous page)
refresh - Refreshes the current page (good for staying up to date with the latest tweets)
browser, (tweet ID) - Opens the selected tweet in the browser.

I am currently working on:
commands:
tweet, text - it... well... tweets
reply, tweet ID, text - do i really need to explain this one too?
link, tweet ID, (link ID) - Opens a link from the selected tweet
media, tweet ID, (media ID), - Opens attached media in the browser

Other:
Fixing broken commands and formatting
making sure the readme doesn't look like a 5 year old wrote it (will come near the end of the project though)
