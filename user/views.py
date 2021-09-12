from rest_framework.views import APIView
from rest_framework.response import Response


class UserView(APIView):
    def get(self, *args, **kwargs):
        return Response('hello from get')
    def post(self, *args, **kwargs):
        return Response('hello from post')
    def patch(self, *args, **kwargs):
        return Response('hello from patch')
    def put(self, *args, **kwargs):
        return Response('hello from put')
    def delete(self, *args, **kwargs):
        return Response('hello from delete')