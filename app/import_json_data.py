#!/usr/bin/python
# coding=utf-8
import os,json
os.environ.update({"DJANGO_SETTINGS_MODULE": "MockServer.settings"})

from .models  import Snippet
# from app.serializers import SnippetSerializer

def a():
    # try:
    #     snippet = Snippet.objects.get(pk=pk)
    # except Snippet.DoesNotExist:
    #     print('Snippet.DoesNotExist')
    #
    # serializer = SnippetSerializer(snippet, data=data)
    # if serializer.is_valid():
    #     serializer.save()


    p=os.path.join(os.getcwd(),'mock.json')
    # print p
    f=open(p,'r').read()#.decode('utf-8')
    # print type(json.loads(f))
    for [k,v] in dict.items(json.loads(f)):
        try:
            snippet = Snippet.objects.get(url=k)
        except Snippet.DoesNotExist:
            snippet=Snippet(url=k,owner=1)
        for [k2,v2] in dict.items(v):
            if(k2=='data'):
                snippet.code=v2
            if(k2=='msg'):
                snippet.title=v2
        snippet.save()

a()