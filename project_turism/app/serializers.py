from django.core.files import images
from rest_framework import serializers


from .models import Post, Pereval_added, Users, Coords, Level, Images, PerevalImages


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =('id', 'title','cover')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'fam', 'name', 'otc', 'phone')

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring')

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('date', 'title',)





class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)
    class Meta:
        model = Pereval_added
        fields = ('beautyTitle', 'title', 'other_titles', 'connect',
                  'add_time', 'status', 'user', 'coords', 'level', 'images')

        def create(self, validated_data):
            print(validated_data)
            images - validated_data.pop('images')
            current_user = validated_data.pop('user')
            ses_email = current_user['email']
            ses_fam = current_user['fam']
            ses_name = current_user['name']
            ses_otc = current_user['otc']
            ses_phone = current_user['phone']
            list_user = Users.objects.all()
            check = False
            for next_user in list_user:
                if next_user.email == ses_email:
                    user_id = next_user
                    check = True
                    break

            if not check:
                Users.object.create(email=ses_email, fam=ses_fam, name=ses_name, otc=ses_otc, phone=ses_phone)
                user_id = Users.objects.filter(email=ses_email)[0]
                print(user_id, type(user_id))

            current_coords = validated_data.pop('coords')
            ses_latitude = current_coords['latitude']
            ses_longitude = current_coords['longitude']
            ses_height = current_coords['height']
            Coords.objects.create(latitude=ses_latitude, longitude=ses_longitude, height=ses_height)
            coord_id = Coords.objects.filter(latitude=ses_latitude)[0]

            # обработка уровня сложности

            current_level = validated_data.pop('level')
            ses_winter = current_level['winter']
            ses_summer = current_level['summer']
            ses_autumn = current_level['autumn']
            ses_spring = current_level['spring']
            Level.objects.craete(winter=ses_winter, summer=ses_summer, autumn=ses_autumn, spring=ses_spring)
            level_id= Level.objects.filer(winter=ses_winter).filter(summer=ses_summer).filter(autumn=ses_autumn).filter(spring=ses_spring)

            # создание записи в таблице перевал

            validated_data.setdefault('user', user_id)
            validated_data.setdefault('coords', coord_id)
            validated_data.setdefault('level', level_id)

            pereval = Pereval_added.objects.create(**validated_data)

            for image in images:
                current_image, status = Images.object.get_or_create(**image)
                PerevalImages.objects.create(images=current_image, pereval=pereval)
            return pereval

        def update(self, instance, validated_data):
            instance.beautyTitle = validated_data.get('beautyTitle')
            instance.btitle = validated_data.get('title')
            instance.other_title = validated_data.get('other_title')
            instance.connect = validated_data.get('connect')
            instance.add_time = validated_data.get('add_time')
            instance.status = validated_data.get('status')
            current_coords = validated_data.get('coords')

            ses_latitude = current_coords['latitude']
            ses_longitude = current_coords['longitude']
            ses_height = current_coords['height']
            Coords.objects.filter(pk=instance.coord_id).update(latitude=ses_latitude, longitude=ses_longitude, height=ses_height)

            current_level = validated_data.get('level')
            ses_winter = current_level['winter']
            ses_summer = current_level['summer']
            ses_autumn = current_level['autumn']
            ses_spring = current_level['spring']
            Level.objects.filer(pk=instance.level_id).update(winter=ses_winter, summer=ses_summer, autunm=ses_spring, spring=ses_autumn)

            instance.save()
            return instance








