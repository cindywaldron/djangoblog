from django.urls import path
from .views import list_view, detail_view, add_model
from myblog.feed import LatestEntriesFeed

urlpatterns = [
    path('',list_view,name="blog_index"),
    path('posts/<int:post_id>/',detail_view, name="blog_detail"),
    path('new_post',add_model, name="new_post"),
    path('latest/feed/', LatestEntriesFeed()),
]
