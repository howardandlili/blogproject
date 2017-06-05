from django.db import models


# Create your models here.

class Category(models.Model):
    '定义分类表'
    name = models.CharField(max_length=32)


class Tag(models.Model):
    '定标签表'
    name = models.CharField(max_length=32)


class User(models.Model):
    '定义用户表'
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    cname = models.CharField(max_length=32,blank=True)

class Post(models.Model):
    '定于文章表'
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)  # 摘要
    category = models.ForeignKey(Category)  # 一对多关系
    tag = models.ManyToManyField(Tag, blank=True)  # 多对多关系
    author = models.ForeignKey(User)
