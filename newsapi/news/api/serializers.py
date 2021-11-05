from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers

from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = JournalistSerializer()

    class Meta:
        model = Article
        exclude = ('id',)

    def get_time_since_publication(self, object: Article):
        return timesince(object.publication_date, datetime.now())

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                'Title and Description must be different.'
                )
        return data

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "The title has to be at least 10 characters long."
            )

        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='article-detail'
    )
    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"

#
# This is going to be much easier with the "ModelSerializers" class. However, he
# wanted us to do this part so we could see exactly how serializing in Django
# REST works.
#
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data) -> Article:
#         print(validated_data)
#         return Article.objects.create(**validated_data)

#     def update(self, instance: Article, validated_data) -> Article:
#         instance.author = validated_data.get("author", instance.author)
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get(
#             "description", instance.description
#         )
#         instance.body = validated_data.get("body", instance.body)
#         instance.location = validated_data.get("location", instance.location)
#         instance.publication_date = validated_data.get(
#             "publication_date", instance.publication_date
#         )
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError(
#                 'Title and Description must be different.'
#                 )
#         return data

#     def validate_title(self, value):
#         if len(value) < 60:
#             raise serializers.ValidationError(
#                 "The title has to be at least 60 characters long."
#             )

#         return value