# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


class IsOwnerOrReadOnly(BasePermission):
    """
    允许创建者编辑的自定义权限
    """

    def has_object_permission(self, request, view, obj):
        # 任何request都有只读权限, 所以总是允许GET, HEAD 或 OPTIONS
        if request.method in SAFE_METHODS:
            return True

        # 只有snippet的创建者有写的权限
        return obj.owner == request.user