from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.TopView.as_view(), name='topview'),
    path('<int:pk>/', views.ListView.as_view(), name='listview'),
    path('<int:pk>/reply/', views.ReplyView.as_view(), name='replyview'),
    path('<int:top_id>/<int:listof_id>/', views.DetailView, name='detailview'),
]
