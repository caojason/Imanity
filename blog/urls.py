from django.urls import path

from . import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    path('view/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView, name='bloggers'),
    path('create/', views.BlogCreate.as_view(), name='blog_create'),
    path('comment/<int:pk>/', views.BlogCommentCreate.as_view(), name='blog_comment'),
]
