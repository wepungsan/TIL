from django.urls import path

from posts import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('new', views.post_create, name='post-create'),
    path('<int:post_id>', views.post_detail, name="post-detail"),
    path('<int:post_id>/edit', views.post_update, name='post-update'),
    path('<int:post_id>/delete', views.post_delete, name='post-delete'),
]
