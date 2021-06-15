from django.shortcuts import render
from django.contrib.auth.models import User,Group
from quickstart.serializers import UserSerializers,GroupSerializers
from rest_framework import viewsets
from django.views import View
from django.http import JsonResponse
from quickstart.models import  Snippet
from quickstart.serializers import SnippetSerializers

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers

class GroupViewSets(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

class savesnippet(View):
    def post(self,req):
        data = req.POST
        serializer = SnippetSerializers(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.save()
            print(Snippet.objects.all())
            return JsonResponse(validated_data)
        else:
            print('chucuo')

    def get(self,req):
        return render(req,'index_quickstart.html')
