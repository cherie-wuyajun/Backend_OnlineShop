#!/usr/bin/env python
# encoding: utf-8
'''
@author: cherie
@contact: cheriewuyajun@hotmail.com
@file: serializers.py
@time: 2019/7/7 0:14
@desc:
'''
import re
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav, UserAddress
from .models import UserLeavingMessage
from goods.serializers import GoodsSerializer

from MxShop.settings import REGEX_MOBILE


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ('goods', 'id')


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message='已经收藏',
            )
        ]

        fields = ('user', 'goods', 'id')


class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ('user', 'message_type', 'subject', 'message', 'file', 'id', 'add_time')


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    province = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    district = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    signer_name = serializers.CharField(required=True)
    signer_mobile = serializers.CharField(max_length=11, min_length=11, required=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ('id', 'user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time')
