from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
    def validate(self, attrs):
        if attrs['title'] == attrs['content']:
            raise serializers.ValidationError("Title and content cannot be the same")
        return attrs
    