from django.urls import path

from .views import ( 
    UserCreateView, 
    CustomObtainAuthTokenView, 
    UserRetrieveUpdateView,
    LogoutView,
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('user/', UserRetrieveUpdateView.as_view(), name='user'),
    path('token/', CustomObtainAuthTokenView.as_view(), name='token'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
