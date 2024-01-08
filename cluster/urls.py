from django.urls import path
from . import views

app_name = 'cluster'

urlpatterns = [
    path('cluster/', views.ClusterView.as_view(), name='cluster_view'),
]
