from django .urls  import  path
from .views import LoginApiView,RegistrationAPIView,CodeVerificationApiView


app_name='users'

urlpatterns=[
    path('login/',LoginApiView.as_view(),name='login'), 
    path('register/',RegistrationAPIView.as_view(),name='register'),
    path('code-verification/',CodeVerificationApiView.as_view(),name='code_verification'),
]