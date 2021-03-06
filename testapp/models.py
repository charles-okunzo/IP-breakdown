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

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image_path = models.ImageField(upload_to='post_images/', blank=True)
    image_name = models.CharField(max_length=20)
    image_caption = models.TextField()
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.image_name}"


class Comment(models.Model):
    content = models.TextField()
    image = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.content}"


class Like(models.Model):
    image = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.user.username} Likes"


#Create followers and follow
class Follow(models.Model):
    account_following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', null=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', null=True)

    def __str__(self) -> str:
        return f"{self.follower}"



# user = User.objects.first()
# user.post_set.all()
#related name => post_set

