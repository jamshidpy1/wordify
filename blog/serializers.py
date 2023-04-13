from rest_framework import serializers
from .models import Category, Tag, Article, SubContent, SubContentImage, Comment


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class MineSubContentImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubContentImage
        fields = ['id', 'image', 'is_wide']


class MineSubContentSerializers(serializers.ModelSerializer):
    subcontentimage = MineSubContentImageSerializers(many=True, read_only=True)

    class Meta:
        model = SubContent
        fields = ['id', 'content', 'subcontentimage']


class ArticleGETSerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    tags = TagSerializers(read_only=True, many=True)
    subcontent = MineSubContentSerializers(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'content', 'subcontent', 'created_date']


class SubContentImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubContentImage
        fields = ['id', 'subcontent', 'image', 'is_wide']


class SubContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubContent
        fields = ['id', 'article', 'content']
        extra_kwargs = {
            'article': {'required': False}
        }

        def create(self, validated_data):
            article_id = self.context['article_id']
            content = validated_data.get('content')
            instance = SubContent.objects.create(article_id=article_id, content=content)
            return instance


class ArticlePOSTSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'category', 'image', 'content', 'tags', 'created_date']
        extra_kwargs = {
            'article': {"read_only": True}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']
        extra_kwargs = {
            'article': {'required': False}
        }

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        author_id = request.user.profile.id
        description = validated_data.get('description')
        instance = Comment.objects.create(article_id=article_id, author_id=author_id, description=description)
        return instance
