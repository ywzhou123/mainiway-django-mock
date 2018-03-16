# -*- coding: utf-8 -*-
from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Snippet
from .serializers import SnippetSerializer

# 分页
from rest_framework.pagination import PageNumberPagination

#通用视图
from rest_framework import generics,viewsets

#权限相关
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer

# 分页
class SnippetListPagination(PageNumberPagination):
	page_size = 10
	page_size_query_param = 'pageSize'
	max_page_size = 100
	page_query_param = 'page'

#viewset视图
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    这一viewset提供了`list`和`detail`
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    这一viewset提供了`list`, `create`, `retrieve`, `update` 和 `destroy`
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # authentication_classes = (authentication.TokenAuthentication,)  # 认证策略属性
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,) # 权限策略属性
    pagination_class = SnippetListPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title','url')
    ordering = ('url', )
    # def pre_save(self, obj):
    #     obj.owner = self.request.user


import execjs,os,time
from django.http import HttpResponse
def Mock(request,url):
    try:
        snippet = Snippet.objects.get(url=request.path)
    except Snippet.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    f=os.path.join(os.getcwd(),'mock.js')
    ctx = execjs.compile(open(f,'r').read().decode('utf-8'))
    time.sleep(snippet.sleep)
    data=ctx.call('getMockData', snippet.code)

    return HttpResponse(data)


# from rest_framework.authtoken.models import Token
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)