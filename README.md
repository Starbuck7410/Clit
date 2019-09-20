# Clit
CLIT - Command Line Interface for Twitter

Uses Python 3, Selenium with Chromedriver (For version 77), Google chrome, and tweepy.


Commands:
Commands are the key to controlling Clit. Some commands require 1 input, which is the command name, and some require more than one (For example the "browser" command). Commands that require more than 1 input recieve the other inputs in a seperate line (So for the "browser" command, you enter "browser", [Enter], and the tweet ID).

Current commands:
exit - Exits Clit
pagedn - Page down, loads the next 5 tweets (next page) (CURRENTLY BROKEN)
pagedn - Page up, loads the previous 5 tweets (previous page) (CURRENTLY BROKEN)
refresh - Refreshes the current page (good for staying up to date with the latest tweets) (CURRENTLY BROKEN)
browser, (tweet ID) - Opens the selected tweet in the browser.

I am currently working on:
commands:
link, (tweet ID), (link ID) - Opens a link from the selected tweet
media, (tweet ID), (media ID), - Opens attached media in the browser

Other:
Fixing broken commands and formatting
