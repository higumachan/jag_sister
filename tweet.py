# -*- coding: utf-8 -*-

import tweepy
import time
import random

def load_tweets():
    f = open("tweets.txt");
    
    return ([row.strip() for row in f]);

if __name__ == "__main__":
    oauth = tweepy.OAuthHandler("vkl9rSrIXB4F6Qp23hHb6g", "BNBLDCAtnc3zsAT7WEnjbSKqVvNQNY6kqCyuC4w5wNI", "581819846-DLncCSJPVCP0BeweVqCLt3lnX1cYbRBoeERHKSbv", "wK2QHDM1jzjUNaYB8peYLlZ1YIZwE7ryIClAtLUh0");
    api = tweepy.API(oauth);
    
    tweets = load_tweets();
    print tweets[0]
    while True:
        tw = tweets[random.randint(0, len(tweets) - 1)];
        print tw
        api.update_status(tw);
        puts("Tweet");
        time.sleep(60 * 60 * 2);


