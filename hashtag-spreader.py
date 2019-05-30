import json
from mastodon import Mastodon, StreamListener


def print_status(status):
    print("time: " + str(status["created_at"]))
    print("from: @" + status["account"]["acct"])

with open("config.json", 'r') as f:
    config = json.load(f)

if config:
    chaos_social = Mastodon(
        access_token = config["source"]["token"],
        api_base_url = config["source"]["url"]
    )

    fem_social = Mastodon(
        access_token = config["drain"]["token"],
        api_base_url = config["drain"]["url"]
    )

    class TootListener(StreamListener):
        def on_update(self, status):
            print("")
            print(" -- new status in " + config["source"]["url"] + " -- ")
            print_status(status)
            #print(status)
            print("")
            print(" -- search in " + config["drain"]["url"] + " -- ")
            try:
                search = fem_social.search(status.url)
                for s in search["statuses"]:
                    print_status(s)
            except:
                print("failed")

    tootListener = TootListener()

    chaos_social.stream_hashtag(config["source"]["hashtag"], tootListener, run_async=False, timeout=300, reconnect_async=False, reconnect_async_wait_sec=5)
