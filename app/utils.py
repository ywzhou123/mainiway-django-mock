# -*- coding: utf-8 -*-
from django.utils import six
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class JsonResponse(Response):
    """
    An HttpResponse that allows its data to be rendered into
    arbitrary media types.
    """

    def __init__(self, data=None, code=None, desc=None,
                 status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        """
        Alters the init arguments slightly.
        For example, drop 'template_name', and instead use 'data'.
        Setting 'renderer' and 'media_type' will typically be deferred,
        For example being set automatically by the `APIView`.
        """
        super(Response, self).__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        self.data = {"code": code, "desc": desc, "data": data}
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import status


def api_paging(objs, request, Serializer):
    """
    objs : 实体对象
    request : 请求对象
    Serializer : 对应实体对象的序列化
    """
    try:
        page_size = int(request.GET.get('page_size', 2))
        page = int(request.GET.get('page', 1))
    except (TypeError, ValueError):
        return JsonResponse(
            code=status.HTTP_400_BAD_REQUEST,
            desc='page and page_size must be integer!'
        )

    paginator = Paginator(objs, page_size) # paginator对象
    total = paginator.num_pages #总页数
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    serializer = Serializer(objs, many=True) #序列化操作

    return JsonResponse(
        data={
            'detail': serializer.data,
            'page': page,
            'total': total
        },
        code=status.HTTP_200_OK,
        desc='page success'
    ) #返回