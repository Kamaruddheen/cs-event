from django.db import models
from wordhunt.models import User


# Student Result Logo
class Logo(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='Logo')
    score = models.PositiveIntegerField(default=0)
    roundtype_choice = (('prelims', 'Prelims'), ('final', 'Finals'))
    roundtype = models.CharField(
        max_length=8, choices=roundtype_choice)
    description = models.TextField(max_length=430)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Logo Result'

# Student Result Poster both prelims & finals


class Poster(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='Poster')
    status = models.BooleanField()
    score = models.PositiveIntegerField(default=0)
    roundtype_choice = (('prelims', 'Prelims'), ('final', 'Finals'))
    roundtype = models.CharField(
        max_length=8, choices=roundtype_choice)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Poster Result'
