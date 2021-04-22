import os
import json
import twarc
import dotenv

from twarc.client2 import Twarc2
from twarc.expansions import flatten

dotenv.load_dotenv()
token = os.environ.get('BEARER_TOKEN')

t = Twarc2(bearer_token=token)

tweets = next(t.search_recent('conversation_id:1385008025140871168'))
del tweets['__twarc']

json.dump(tweets, open('example.json', 'w'), indent=2, sort_keys=True)
json.dump(flatten(tweets), open('example-flat.json', 'w'), indent=2, sort_keys=True)


