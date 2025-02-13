from django.db import models

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return f'{self.title}'


class Users(models.Model):
    email = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.email}{self.fam}{self.name}{self.otc}{self.phone}'

class Coords(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.latitude}{self.longitude}{self.height}'

class Level(models.Model):
    winter = models.CharField(max_length=255)
    summer = models.CharField(max_length=255)
    autumn = models.CharField(max_length=255)
    spring = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.winter}{self.summer}{self.autumn}{self.spring}'

class Images(models.Model):
    data = models.TextField()
    title = models.CharField(max_length=255)

class Pereval_added(models.Model):
    new = 'Добавлено'
    pending = 'На рассмотрении'
    accepted = 'Принято'
    rejected = 'Отклонено'
    VERIF_STATUS =[
        (new,'Добавлено'),
        (pending,'На рассмотрении'),
        (accepted,'Принято'),
        (rejected,'Отклонено'),
    ]
    beautyTitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField()
    status = models.CharField(max_length=255, choices=VERIF_STATUS, default=new)
    user = models.ForeignKey(Users, related_name='per_user', on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, related_name='per_coords', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name='per_level', on_delete=models.CASCADE)
    images = models.ManyToManyField(Images, through='PerevalImages')

class PerevalImages(models.Model):
    pereval = models.ForeignKey(Pereval_added, on_delete=models.CASCADE)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pereval}{self.images}'


