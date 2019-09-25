import time
import os
import tweepy
from selenium import webdriver

#Globals:
#pagenum, timeline, CONSUMER_TOKEN, CONSUMER_SECRET



def get_api_keys():
    
    file = open("env.txt","r")
    api_keys = file.read()
    file.close()
    
    global CONSUMER_TOKEN
    global CONSUMER_SECRET
    
    CONSUMER_TOKEN = api_keys[:25]
    CONSUMER_SECRET = api_keys[26:]


class TwitterOAuthTool:

    def __init__(self):
        self.auth = None
        self.access_token = None
        self.access_token_secret = None

    def get_authorization_url(self):

        redirect_url = None
        self.auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
        try:
            redirect_url = self.auth.get_authorization_url()
        except (tweepy.TweepError, e):
            print ('Error! Failed to get request token.')
        return redirect_url

    def get_token_and_secret(self, verifier_code):

        try:
            self.auth.get_access_token(verifier_code)
        except tweepy.TweepError:
            print ('Error! Failed to get access token.')
            return None

        self.access_token = self.auth.access_token
        self.access_token_secret = self.auth.access_token_secret
        return (self.access_token, self.access_token_secret)

    def verify_authorization(self):

        auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api

    def update_tokens(self, recieved_token, recieved_secret_token):
        self.access_token = recieved_token
        self.access_token_secret = recieved_secret_token
        return


def log_in():
    tool = TwitterOAuthTool()
    if (not os.path.exists("authkey.txt")):
        auth_url = tool.get_authorization_url()
        browser = webdriver.Chrome(executable_path = (os.getcwd() + "\chromedriver\chromedriver.exe"))
        browser.get(auth_url)
        while (browser.current_url[:36] != "https://github.com/Starbuck7410/Clit"):
            time.sleep(3)
        url = browser.current_url
        browser.close()
        verifier_code = url[92:]
        (token, secret) = tool.get_token_and_secret(verifier_code)
        if (token and secret):
            api = tool.verify_authorization()
            print ('User @%s successfully logged in.' %api.me().screen_name)

        else:
            print ('Failed to get the key and secret for the user. Please run the program again to retry.')
            exit()
            
        print("Would you like to save the login credentials? (Y/N)")
        ans = input()
        if (ans == "Y"):
            file = open("authkey.txt","w+")
            file.write(token + "/" + secret)
            file.close()
    else:
        file = open("authkey.txt","r")
        keys = file.read()
        file.close()
        token = keys[:50]
        secret = keys[51:]
        tool.update_tokens(token, secret)
        api = tool.verify_authorization()
        print ('User @%s successfully logged in.' %api.me().screen_name)
        print()
    return api

def exe(cmd):
    global pagenum

    if (cmd == "exit"):
        exit()
        return
        
    if (cmd == "pagedn"):
        pagenum += 1
        tl(int(pagenum))
        return
    
    if (cmd == "pageup"):
        pagenum -= 1
        tl(int(pagenum))
        return
    
    if (cmd == "refresh"):
        tl(pagenum)
        return
    
    if (cmd == "page"):
        pagenum = input("PAGE:\>")
        tl(pagenum)
        return
#    if (cmd == "link"):
#        tweet = int(input())
#        urlindex = int(input())
#        url = timeline[tweet].entities["urls"][urlindex]
#        browser = webdriver.Chrome(executable_path = (os.getcwd() + "\chromedriver\chromedriver.exe"))
#        browser.get(url)
#    if (cmd == "media"):
#        tweet = int(input())
#        mediaindex = int(input())
#        url = timeline[tweet].entities["media"][mediaindex]["media_url"]
#        browser = webdriver.Chrome(executable_path = (os.getcwd() + "\chromedriver\chromedriver.exe"))
#        browser.get(url)
    if (cmd == "browser"):
        tweet = int(input("ID:\>"))
        browser = webdriver.Chrome(executable_path = (os.getcwd() + "\chromedriver\chromedriver.exe"))
        browser.get("https://twitter.com/" + timeline[tweet].user.screen_name + "/status/" + str(timeline[tweet].id))
        return
    
    if (cmd == "tweet"):
        text = input("TEXT:\>")
        api.update_status(text)
        print("You have succesfully tweeted!")
        return
    
    if (cmd == "reply"):
        num = input("ID:\>")
        text = input("TEXT:\>")
        api.update_status(text, timeline[int(num)].id)
        return
    
    if (cmd == "help"):
        file = open("readme.md","r")
        help = file.read()
        file.close()
        print(help)
        return
        
#    if (cmd == "id"):
#        num = input()
#        print(timeline[int(num)].id)
    print("Error: command \"%s\" was not found." %cmd)
    return

def tl(page):
    global timeline
    global pagesize
    pagesize = 5
    timeline = api.home_timeline(count = pagesize, page = page)
    print("\n ~~~~~~~~~~~~~~~~~~ \n")
    for id in range(len(timeline)):
        print("Tweet ID: %i" %id)
        print(timeline[id].user.name + " (" + timeline[id].user.screen_name + ") tweeted:")
        print(timeline[id].text)
#        if (not timeline[id].entities["media"][0] == ""):
#            print("(Has media)")
        print("\n ~~~~~~~~~~~~~~~~~~ \n")
    print("End of page %i." %(page))

if '__main__' == __name__:
    print("Logging in, please wait...")
    get_api_keys()
    api = log_in()
    pagenum = 1
    tl(pagenum)
    while (True):
        command = input("CLIT:\>")
        exe(command)
    
    
