import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json_performer
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_json():
    """
    Getts json object with user's friend's info
    """
    acct = input('Enter Twitter Account:')
    if len(acct) < 1:
        return None
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    return js


json_performer.interact_with_user(get_json())
