from django.db import models

# Create your models here.
class Task(models.Model):
    class FlatFormChoice(models.TextChoices):
        mobie = 'mobie','Di động'
        chrome = 'chrome','Google Chrome'
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=255,choices=FlatFormChoice.choices)
    nodes = models.JSONField()
    edges = models.JSONField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('account.Account',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
