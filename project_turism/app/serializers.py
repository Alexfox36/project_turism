from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields =('id', 'title','cover')