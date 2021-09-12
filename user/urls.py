from django.urls import path
from .views import UserCreateListView, UserRetriveUpdateDeleteView


urlpatterns = [
    path('', UserCreateListView.as_view(), name= 'user_list_create'),
    path('/<int:pk>', UserRetriveUpdateDeleteView.as_view(),name='user_retrive_update_delete')
]