from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()

# post1 = Post.objects.create(name='man', city='siamese', description='loud', age=35)
# post2 = Post.objects.create(name='man1', city='siamese', description='loud', age=44)
# post3 = Post.objects.create(name='man2', city='siamese', description='loud', age=18)

# posts = [post1, post2, post3]
