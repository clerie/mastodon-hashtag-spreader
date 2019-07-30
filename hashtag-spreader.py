#!/usr/bin/env python3

import json
from threading import Thread
from mastodon import Mastodon, StreamListener


def print_status(status):
    print("time: " + str(status["created_at"]))
    print("from: @" + status["account"]["acct"])

class TootListener(StreamListener):
    def __init__(self, source, drain):
        self.source = source
        self.drain = drain

    def on_update(self, status):
        print("")
        print("--")
        print("RECIEVE " + self.source.api_base_url + "")
        print_status(status)
        print("SEARCH " + self.drain.api_base_url + "")
        try:
            search = self.drain.search(status.url)
            for s in search["statuses"]:
                print_status(s)
        except:
            print("failed")
        print("--")

class HashtagSpreader(Thread):
    def __init__(self, source, drain, hashtag):
        Thread.__init__(self)

        self.source = source
        self.drain = drain
        self.hashtag = hashtag

    def run(self):
        tootListener = TootListener(self.source, self.drain)
        self.source.stream_hashtag(self.hashtag, tootListener)

if __name__ == "__main__":
    instances = {}
    threads = []

    with open("config.json", 'r') as f:
        config = json.load(f)

    if config:
        for instance in config["instances"]:
            instances[instance] = Mastodon(access_token = config["instances"][instance], api_base_url = "https://" + instance)

        for spread in config["spreads"]:
            if spread["source"] in instances and spread["drain"] in instances:
                for hashtag in spread["hashtags"]:
                    threads.append(HashtagSpreader(instances[spread["source"]], instances[spread["drain"]], hashtag))


    for thread in threads:
        thread.start()
