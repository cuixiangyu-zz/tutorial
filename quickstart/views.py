from django.shortcuts import render
from django.contrib.auth.models import User,Group
from quickstart.serializers import UserSerializers,GroupSerializers
from rest_framework import viewsets

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers

class GroupViewSets(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers