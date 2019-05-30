import json
from mastodon import Mastodon, StreamListener

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
            print(" -- new status in chaos.social -- ")
            print(status)
            print("")
            print(" -- search in fem.social -- ")
            print(fem_social.search(status.url))

    tootListener = TootListener()

    chaos_social.stream_hashtag(config["source"]["hashtag"], tootListener, run_async=False, timeout=300, reconnect_async=False, reconnect_async_wait_sec=5)
