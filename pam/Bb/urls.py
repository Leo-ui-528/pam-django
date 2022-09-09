from django.urls import path
from .views import index, by_owner, BbCreateView

urlpatterns = [
    path('<int:owner_id>/', by_owner, name='by_owner'),
    path('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
]
