from django.db import models
from userapp.models import User


class question_model(models.Model):
    question = models.CharField(max_length=450)
    option_A = models.CharField(max_length=30)
    option_B = models.CharField(max_length=30)
    option_C = models.CharField(max_length=30)
    option_D = models.CharField(max_length=30)
    correct_option = models.CharField(max_length=30)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Prelims Aptitude Question'


class Stud_Res_CodeTreasure_Prelm(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(question_model, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=30)
    status = models.BooleanField()
    when = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Student Result Prelim'


# final round code shuffling
class final_code_shuffle(models.Model):
    image = models.ImageField(upload_to='final_code_shuffle/')

    class Meta:
        verbose_name = 'Code Shuffle Image'


class final_code_shuffle_relation(models.Model):
    question = models.ManyToManyField(final_code_shuffle)
    ques_no = models.CharField(max_length=80, default="Codeshuffle")

    def __str__(self):
        return self.ques_no

    class Meta:
        verbose_name = 'Code Shuffle Question'


# Final round binary
class final_code_binary_question(models.Model):
    question = models.CharField(max_length=250)
    ques_no = models.CharField(max_length=80, default="Binaryhunt")

    def __str__(self):
        return self.ques_no

    class Meta:
        verbose_name = 'Binary Hunter Question'


# Final round spot the error
class final_code_spot_error_image(models.Model):
    image = models.ImageField(upload_to="final_code_spot_error/")

    class Meta:
        verbose_name = 'Spot Error Image'


class final_code_spot_error_question(models.Model):
    question = models.ManyToManyField(final_code_spot_error_image)
    ques_no = models.CharField(max_length=80, default="SpotError")

    def __str__(self):
        return self.ques_no

    class Meta:
        verbose_name = 'Spot Error Question'


# Final round question's relation with the user's answer
class final_answer_relation(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    final_code_shuffle_question = models.ForeignKey(
        final_code_shuffle_relation, on_delete=models.CASCADE, null=True)
    final_code_binary_question = models.ForeignKey(
        final_code_binary_question, on_delete=models.CASCADE, null=True)
    final_code_spot_error_question = models.ForeignKey(
        final_code_spot_error_question, on_delete=models.CASCADE, null=True)
    user_answer = models.TextField()
    when = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Student Result Final'


class Score_codetreasureModel(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    roundtype_choice = (('prelims', 'Prelims'), ('final', 'Finals'))
    roundtype = models.CharField(max_length=8, choices=roundtype_choice)
    score = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Score'
