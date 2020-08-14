from django.db import models

class videocategory(models.Model):
    name = models.CharField(max_length=20, default=1)

    @staticmethod
    def get_all_videocategories():
        return videocategory.objects.all()

    def __str__(self):
        return self.name
