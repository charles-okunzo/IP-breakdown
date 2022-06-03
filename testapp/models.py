from django.db import models

# Create your models here.

# User model
# Profile
# Image/Post
# Comment
from django.db import models
from django.contrib.auth.models import User


# class User:
#     pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', default= 'default.jgp')
    bio = models.TextField()


    def __str__(self) -> str:
        return f"{self.user.username} Profile"

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='post_images/', blank=True)
    image_name = models.CharField(max_length=20)
    image_caption = models.TextField()
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.image_name}"


class Comment(models.Model):
    content = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.content}"


class Like(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.user.username} Likes"


#Create followers and follow
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE)
    # follower = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.following}"

