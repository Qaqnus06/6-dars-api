from django. urls import path
from .views import CardsApiView,OneCardApiView

urlpatterns=[
    path('cards/',CardsApiView.as_view(),name='cards'), 
    path('one-card/',OneCardApiView.as_view(),name='one-card'),
    
]