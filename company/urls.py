from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.List.as_view(), name='list'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('delete/', views.Delete.as_view(), name='delete'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('industry/<int:industry>', views.Industry.as_view(), name='industry'),
    path('cluster_list/<int:cluster>', views.Cluster.as_view(), name='cluster')
]