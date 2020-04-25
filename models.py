from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)#图书名称
    bpub_date = models.DateField()#发布日期
    bread = models.IntegerField(default=0)#阅读量
    bcomment = models.IntegerField(default=0)#评论量
    isDelete = models.BooleanField(default=False)#逻辑删除

class Register(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length = 128)
	phonenumber = models.CharField(max_length = 11)
