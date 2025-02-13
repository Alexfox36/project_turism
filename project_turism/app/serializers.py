from rest_framework import serializers
from tutorial.quickstart.serializers import UserSerializer

from .models import Post, Pereval_added


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields =('id', 'title','cover')




class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)
    class Meta:
        model = Pereval_added
        fields = ('beautyTitle', 'title', 'other_titles', 'connect',
                  'add_time', 'status', 'user', 'coords', 'level', 'images')

