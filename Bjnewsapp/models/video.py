from django.db import models
from embed_video.fields import EmbedVideoField
from .videocategory import videocategory

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    videocategory = models.ForeignKey(videocategory, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=500, default=1)

    @staticmethod
    def get_all_items_by_videocategoryid(videocategory_id):
        if videocategory_id:
            return Item.objects.filter(videocategory = videocategory_id)
        else:
            return Item.get_all_items();

    @staticmethod
    def get_all_items():
        return Item.objects.all()
