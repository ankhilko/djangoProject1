from django.urls import path
from .views import blog_list, post_detail, contact, about, PostListView, PostDetailView

urlpatterns = [
    # path('', blog_list, name='blog_posts'),
    path('', PostListView.as_view(), name='blog_posts'),
    path('contact/', contact, name='blog_contact'),
    path('about/', about, name='blog_about'),
    # path('<slug:post_slug>/', post_detail, name='blog_post'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='blog_post'),

]
