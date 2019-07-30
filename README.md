# Mastodon Hashtag Spreader

For [#GPN19](https://entropia.de/GPN19) my Mastodon instance [fem.social](https://fem.social) wants to get all posts for this hashtag. Most users at this event are connected to the instance [chaos.social](https://chaos.social).

## Our solution
We have a script on one of our servers which streams all posts for specific hashtag from [chaos.social](https://chaos.social) and puts the URLs of those posts into the search entry of our own instance. Thus, the URLs will get fetched by our instance and the posts is added to our hashtag timeline.

## Installation
```bash
pip3 install Mastodon.py
git clone https://github.com/clerie/mastodon-hashtag-spreader.git
cd mastodon-hashtag-spreader/
cp config.json.example config.json
nano config.json
```
Edit config for your needs.
```bash
python3 hashtag-spreader.py
```

## Scopes
To get this script work, you need an application token on each instance you want to get connected to.
The needed scopes are depending on the role of the instace.

### Source
* `read:statuses`

### Drain
* `read:search`
