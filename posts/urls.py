# Going forward whenever we want to switch between user accounts we’ll need to jump
# into the Django admin, log out of one account and log in to another. Each and every
# time. Then switch back to our API endpoint.
# This is such a common occurrence that Django REST Framework has a one-line
# setting to add log in and log out directly to the browsable API itself. We will implement
# that now.

from django.urls import path

from .views import PostList, PostDetail

urlpatterns = [
path('<int:pk>/', PostDetail.as_view()),
path('', PostList.as_view()),
]