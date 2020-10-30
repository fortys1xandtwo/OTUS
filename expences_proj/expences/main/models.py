from django.db import models


class TestModel(models.Model):

    name = models.CharField(max_length=64, default='')
    type = models.IntegerField(null=False)

    def __str__(self):
        return self.name
