from django.db import models


class ApiModel(models.Model):
    TYPE_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3")
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
