from django.db import models

# Create your models here.
class Category(models.Model):
    board_name = models.CharField(max_length=50, unique=True) # 백엔드에서 식별하기 위해 쓰는 것
    showing_name = models.CharField(max_length=50,) # 사용자들에게 보여주는 것
    ordering = models.FloatField()

    def __str__(self):
        return self.board_name

    class Meta:
        ordering = ['-ordering']