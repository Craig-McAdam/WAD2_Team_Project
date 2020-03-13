from django.db import models
from django.contrib.auth.models import User
#from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    date_of_birth = models.DateField
    profile_image = models.ImageField(upload_to='profile_images', blank=True)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user.username


class Game(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=64)
    release_date = models.DateField
    category = models.CharField(max_length=64)
    system = models.CharField(max_length=64)
    developer = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    age_rating = models.CharField(max_length=3, default='TBA')
    cover_art = models.ImageField(upload_to='cover_art', blank=True)

    # slug_name has to unique for each game for urls to work properly
    #name_slug = models.SlugField(unique=True)
    #def save(self, *args, **kwargs):
    #    self.name_slug = slugify(self.name)
    #    super(Game, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.id + self.name


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Favourites'

    def __str__(self):
        return self.user.__str__() + self.game.__str__()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField
    comment = models.CharField(max_length=128)
    time_posted = models.DateTimeField
    #helpfulness = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.user.__str__() + self.game.__str__()