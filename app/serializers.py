# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
	#source参数控制着使用snippet哪个attribute作为来源填充该field,只读
	# owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'url', 'code' ,'sleep', 'created')


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	#"snippets"是User的一个反向关系
	# snippets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('id', 'username')