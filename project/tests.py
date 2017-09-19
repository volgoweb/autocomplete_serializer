from django.test import TestCase

from .models import Article, Category, Post
from .serializers import AutoCompleteSerializer


class TestSerializer(TestCase):
    def test_articles(self):
        self.article_initial = ['Article %d' % i for i in range(1, 3)]
        articles = [Article(title=title) for title in self.article_initial]
        Article.objects.bulk_create(articles)

        ser = AutoCompleteSerializer(Article.objects.all(),
                                     id_field_name='id', name_field_name='propname', many=True)
        right_result = {i + 1: title for i, title in enumerate(self.article_initial)}
        self.assertEqual(ser.data, right_result)

    def test_categories(self):
        self.category_initial = ['Category %d' % i for i in range(1, 3)]
        categories = [Category(name=name) for name in self.category_initial]
        Category.objects.bulk_create(categories)

        ser = AutoCompleteSerializer(Category.objects.all(),
                                     id_field_name='id', name_field_name='name', many=True)
        right_result = {i + 1: name for i, name in enumerate(self.category_initial)}
        self.assertEqual(ser.data, right_result)

    def test_posts_with_uuid_identity(self):
        self.post_initial = ['Post %d' % i for i in range(1, 3)]
        posts = [Post(title=title) for title in self.post_initial]
        Post.objects.bulk_create(posts)

        ser = AutoCompleteSerializer(Post.objects.all(),
                                     id_field_name='id', name_field_name='propname', many=True)
        right_result = {str(obj.id): obj.propname for obj in Post.objects.all()}
        self.assertEqual(ser.data, right_result)
