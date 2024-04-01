from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        postRating = self.post_set.aggregate(sum_post_rating=Sum('post_rating'))
        cnt_post_rat = 0
        cnt_post_rat += postRating.get('sum_post_rating')

        comRating = self.author.comment_set.aggregate(sum_com_rating=Sum('com_rating'))
        cnt_com_rat = 0
        cnt_com_rat += comRating.get('sum_com_rating')

        self.rating = cnt_post_rat * 3 + cnt_com_rat
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)

article = "ar"
new = "nw"
ptype = [(article, "Статья"),
         (new, "Новость")]

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=20, choices=ptype)
    post_data_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=20)
    text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating+=1
        self.save()

    def dislike(self):
        self.post_rating-=1
        self.save()

    def previev(self):
        print(self.text[0:123]+"...")

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    com_author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    com_data_time = models.DateTimeField(auto_now_add=True)
    com_rating = models.IntegerField(default=0)

    def like(self):
        self.com_rating+=1
        self.save()

    def dislike(self):
        self.com_rating-=1
        self.save()