from django.db import models
from userapp.models import User

# Create your models here.
class prelim_test(models.Model):
    Student=models.ForeignKey(User,on_delete=models.CASCADE)
    
    event_choice=[('word hunt','Word Hunt'),('code treasure','Code Treasure'),('logo design','Logo Design'),('poster design','Poster Design')]
    event=models.CharField(max_length=20,choices=event_choice)
    
    start=models.DateTimeField(null=True)
    end=models.DateTimeField(null=True)
    
    status=[('started','started'),('finished','finished'),('cheated','cheated'),('not started','not started')]
    test_status=models.CharField(max_length=20,choices=status)
    
    attended=models.BooleanField(default=False)

class final_test(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)

    event_choice=[('word hunt','Word Hunt'),('code treasure','Code Treasure'),('logo design','Logo Design'),('poster design','Poster Design')]
    event=models.CharField(max_length=20,choices=event_choice)

    placed_choice=[('selected','selected'),(1,1),(2,2),(3,3),(4,4),(5,5)]
    placed=models.CharField(max_length=20,choices=placed_choice)

    start=models.DateTimeField()
    end=models.DateTimeField()

    status=[('started','started'),('finished','finished'),('seated','seated'),('not started','not started')]
    test_status=models.CharField(max_length=20,choices=status)

    attended=models.BooleanField()


class test_timings(models.Model):
    event_choice=[('word hunt','Word Hunt'),('code treasure','Code Treasure'),('logo design','Logo Design'),('poster design','Poster Design')]
    event=models.CharField(max_length=20,choices=event_choice)

    round_choice=[('preliminary','preliminary'),('final','final')]
    round_type=models.CharField(max_length=20,choices=round_choice)

    start=models.DateTimeField()
    end=models.DateTimeField()

