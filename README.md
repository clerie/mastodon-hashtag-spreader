# Mastodon Hashtag Spreader

For the #GPN19 my Mastodon instance fem.social wants to get all posts of the hashtag. Most users of this event are connected to the instance chaos.social.

## Our solution
We have a script on one of our servers, streaming all posts of one hashtag from chaos.socail and putting the url of the post to the search entry of our own instance. The url will get fetched by our instace and the resulting post is added to our hashtag timeline.

## Installing
```
pip3 install Mastodon.py
git clone https://github.com/clerie/mastodon-hashtag-spreader.git
cd mastodon-hashtag-spreader/
python3 hashtag-spreader.py
```
