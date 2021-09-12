from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import UserModel


class UserCreateListView(APIView):
    def get(self, *args, **kwargs):
        users = UserModel.objects.all().values()
        return Response(users)
    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        user = UserModel.objects.create(**data)
        return Response(model_to_dict(user))
class UserRetriveUpdateDeleteView (APIView):
    def get(self,*args,**kwargs):
        pk = kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('User with this id is not exist')
        user = UserModel.objects.get(pk=pk)
        return Response(model_to_dict(user))

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('User with this id is not exist')
        data = self.request.data.dict()
        UserModel.objects.filter(pk=pk).update(**data)
        return Response('updated')
    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('User with this id is not exist')
        user = UserModel.objects.get(pk=pk)
        user.delete()

        return Response('deleted')