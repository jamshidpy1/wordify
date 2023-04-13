from django.urls import path
from .views import CategoryListCreateAPIView, TagListCreateAPIView, CategoryRUDAPIView, TagRUDAPIView,\
    ArticleListCreateAPI, ArticleRUDAPI, CommentListCreateAPI, SubContentListCreateAPI, SubImageListCreateAPI


urlpatterns = [
    path('category-list-create/', CategoryListCreateAPIView.as_view()),
    path('category-rud/<int:pk>/', CategoryRUDAPIView.as_view()),
    path('tag-list-create/', TagListCreateAPIView.as_view()),
    path('tag-rud/<int:pk>/', TagRUDAPIView.as_view()),
    path('list-article/', ArticleListCreateAPI.as_view()),
    path('rud-article/<int:pk>/', ArticleRUDAPI.as_view()),
    path('article/<int:article_id>/comment-list-create/', CommentListCreateAPI.as_view()),
    path('article/<int:article_id>/content-list-create/', SubContentListCreateAPI.as_view()),
    path('article/<int:article_id>/content-list-create/image/', SubImageListCreateAPI.as_view()),


]