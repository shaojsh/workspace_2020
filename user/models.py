from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, null=False)
    email = models.CharField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)

    def __repr__(self):
        return "".format(self.id, self.name)

    __str__ = __repr__


class BlogPost(models.Model):
    class Meta:
        ordering = ('-id',)  # 逆序排列
        db_table = 'BlogPost'

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=1, null=False)
    blogNet = models.CharField(max_length=148, null=False)
    des = models.CharField(max_length=500, null=False)

    def __repr__(self):
        return "".format(self.id)

    __str__ = __repr__
