#!/usr/bin/env python3

import json
from threading import Thread
from mastodon import Mastodon, StreamListener


def print_status(status):
    print("time: " + str(status["created_at"]))
    print("from: @" + status["account"]["acct"])

class TootListener(StreamListener):
    """
    Listener class, handling incoming statuses
    """
    def __init__(self, source, drain):
        self.source = source # Source instance Mastodon object
        self.drain = drain # Drain instance Mastodon object

    def on_update(self, status):
        # Just printing some stuff to make it look beautiful in terminal
        # More for debugging than anything else
        print("")
        print("--")
        print("RECIEVE " + self.source.api_base_url + "")
        print_status(status)
        print("SEARCH " + self.drain.api_base_url + "")

        # Searching for the URL of the incoming status in our drain instance
        try:
            search = self.drain.search(status.url)
            for s in search["statuses"]:
                print_status(s)
        except:
            print("failed")

        print("--")

class HashtagSpreader(Thread):
    """
    Thread class, streaming one hashtag from one the source instance and searching for the post URL in the drain instance
    """
    def __init__(self, source, drain, hashtag):
        Thread.__init__(self) # Configure the thread

        self.source = source # Source instance Mastodon object
        self.drain = drain # Drain instance Mastodon object
        self.hashtag = hashtag # The hashtag (without #) as a string, we want to stream

    def run(self):
        tootListener = TootListener(self.source, self.drain)
        self.source.stream_hashtag(self.hashtag, tootListener) # Stream our hashtag


if __name__ == "__main__":
    instances = {}
    threads = []

    with open("config.json", 'r') as f:
        config = json.load(f)

    if config:
        # Create Mastodon objects for every instance
        for instance in config["instances"]:
            instances[instance] = Mastodon(access_token = config["instances"][instance], api_base_url = "https://" + instance)

        # Create threads for every hashtag of a relation
        for spread in config["spreads"]:
            if spread["source"] in instances and spread["drain"] in instances:
                for hashtag in spread["hashtags"]:
                    threads.append(HashtagSpreader(instances[spread["source"]], instances[spread["drain"]], hashtag))

    # Start all threads
    for thread in threads:
        thread.start()
