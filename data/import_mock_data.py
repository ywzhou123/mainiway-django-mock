import json
import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MockServer.settings")
import django
django.setup()

from app.models import Snippet

p = os.path.join(os.getcwd(), 'mock.json')
f = open(p, 'r').read().decode('utf-8')

for [k, v] in dict.items(json.loads(f)):
    try:
        snippet = Snippet.objects.get(url=k)
    except Snippet.DoesNotExist:
        snippet = Snippet(url=k)
        for [k2, v2] in dict.items(v):
            if (k2 == 'data'):
                snippet.code = json.dumps(v2)
            if (k2 == 'msg'):
                snippet.title = v2
            if (k2 == 'sleep'):
                snippet.sleep = v2
    snippet.save()
