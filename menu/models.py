from django.db import models

# Create your models here.


class MenuTree(models.Model):
    title = models.CharField(max_length=100)
    parent = models.IntegerField(null=True)
    menuName = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title} {self.menuName}'
