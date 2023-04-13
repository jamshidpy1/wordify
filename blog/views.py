from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Category, Tag, Article, Comment, SubContent, SubContentImage
from .serializers import ArticleGETSerializers, ArticlePOSTSerializers, CategorySerializers, TagSerializers, \
    CommentSerializers, \
    SubContentSerializers, SubContentImageSerializers, MineSubContentSerializers
from .permissions import IsAdminUserOrReadonly


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUserOrReadonly]


class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    permission_classes = [IsAdminUserOrReadonly]


class ArticleListCreateAPI(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGETSerializers
        return ArticlePOSTSerializers


class ArticleRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [IsAdminUserOrReadonly]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGETSerializers
        return ArticlePOSTSerializers


class SubContentListCreateAPI(generics.ListCreateAPIView):
    queryset = SubContent.objects.all()

    def get_queryset(self, *args, **kwargs):
        on = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            on = on.filter(article_id=article_id)
            return on
        return []

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MineSubContentSerializers
        return SubContentSerializers

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx


class SubImageListCreateAPI(generics.ListCreateAPIView):
    queryset = SubContentImage.objects.all()
    serializer_class = SubContentImageSerializers


class CommentListCreateAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        bir = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            bir = bir.filter(article_id=article_id)
            return bir
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx
