from django.db import models
from userapp.models import User


class Images(models.Model):
    image = models.ImageField(upload_to="Wordhunt/")


# Question for WordHunt Prelims & Final
class Wordhunt(models.Model):
    images = models.ManyToManyField(Images)
    correct_answer = models.CharField(max_length=25)
    section_choice = (('A', 'A'), ('B', 'B'))
    section = models.CharField(max_length=1, choices=section_choice)
    roundtype_choice = (('prelims', 'Prelims'), ('final', 'Finals'))
    roundtype = models.CharField(max_length=8, choices=roundtype_choice)

    class Meta:
        verbose_name = 'Wordhunt'


# Student Result for WordHunt Prelims & Final
class Stud_Res_WordHunt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Wordhunt, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=30)
    status = models.BooleanField()
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Student Result WordHunt'
