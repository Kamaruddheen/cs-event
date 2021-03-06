from django.db import models
from userapp.models import User
# Create your models here.
class question_model(models.Model):
    question = models.CharField(max_length=100)
    option_A = models.CharField(max_length=30)
    option_B = models.CharField(max_length=30)
    option_C = models.CharField(max_length=30)
    option_D = models.CharField(max_length=30)
    correct_option = models.CharField(max_length=30)

    def __str__(self):
        return self.question

class Stud_Res_CodeTreasure_Prelm(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    question=models.ForeignKey(question_model,on_delete=models.CASCADE)
    user_answer=models.CharField(max_length=30)
    status=models.BooleanField()
    when=models.DateTimeField(auto_now_add=True)


