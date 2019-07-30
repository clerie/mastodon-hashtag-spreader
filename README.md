# Mastodon Hashtag Spreader

For the #GPN19 my Mastodon instance [fem.social](https://fem.social) wants to get all posts of the hashtag. Most users of this event are connected to the instance [chaos.social](https://chaos.social).

## Our solution
We have a script on one of our servers, streaming all posts of one hashtag from chaos.social and putting the URL of the post to the search entry of our own instance. The URL will get fetched by our instance and the resulting post is added to our hashtag timeline.

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
