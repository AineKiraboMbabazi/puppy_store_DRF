from django.urls import path
from .views import puppies

urlpatterns = [
    path("api/v1/puppies/<int:pk>", puppies.get_delete_update_puppy, name='get_delete_update_puppy'),
    path("api/v1/puppies/", puppies.get_post_puppies, name='get_post_puppies'),
   
]