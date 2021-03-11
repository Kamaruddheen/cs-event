from django.db import models

from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.fields import BooleanField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=35)
    mobile = models.CharField(
        unique=True, max_length=10, null=True, blank=False)
    user_type_choice = ((1, 'Admin'), (2, 'Staff'), (3, 'Students'))
    user_type = models.PositiveSmallIntegerField(choices=user_type_choice, default=3
                                                 )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']


class StudentModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to=models.Q(user_type=3),
        related_name='student')
    college = models.CharField(max_length=60)
    dept = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=15)
    id_proof = models.ImageField(
        upload_to="Student_id", help_text="Don't have Id Card, then get signature from your college")
    profile_pic = models.ImageField(upload_to="Student_pic")
    bonafide = models.FileField(
        upload_to="Student_bonafide", null=True)  # optional
    college_address = models.TextField(max_length=150)
    address = models.TextField(max_length=150)
    # Events selected
    is_ransack = BooleanField(default=False)
    is_codetreasure = BooleanField(default=False)
    is_impreza = BooleanField(default=False)
    is_webdodger = BooleanField(default=False)
    is_geekspeak = BooleanField(default=False)

    class Meta:
        verbose_name = 'Student'


class prelim_test(models.Model):
    Student = models.ForeignKey(User, on_delete=models.CASCADE)

    event_choice = [('wordhunt', 'Word Hunt'), ('codetreasure', 'Code Treasure'),
                    ('logo', 'Logo Design'), ('poster', 'Poster Design')]
    event = models.CharField(max_length=20, choices=event_choice)

    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    status = [('started', 'started'), ('finished', 'finished'),
              ('cheated', 'cheated'), ('not_started', 'not started')]
    test_status = models.CharField(max_length=20, choices=status)

    attended = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Prelims Test'


class final_test(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    event_choice = [('wordhunt', 'Word Hunt'), ('codetreasure', 'Code Treasure'),
                    ('logo', 'Logo Design'), ('poster', 'Poster Design'), ('ppt', 'Paper Presentation')]
    event = models.CharField(max_length=20, choices=event_choice)

    placed_choice = [('selected', 'Selected'), ('notselected', 'Not Selected'), (1, 1),
                     (2, 2), (3, 3), (4, 4), (5, 5)]
    placed = models.CharField(max_length=20, choices=placed_choice)

    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    status = [('started', 'started'), ('finished', 'finished'),
              ('cheated', 'cheated'), ('not_started', 'not started')]
    test_status = models.CharField(max_length=20, choices=status)

    attended = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Finals Test'


class test_timings(models.Model):
    event_choice = [('wordhunt', 'Word Hunt'), ('codetreasure', 'Code Treasure'),
                    ('logo', 'Logo Design'), ('poster', 'Poster Design'), ('ppt', 'Paper Presentation')]
    event = models.CharField(max_length=20, choices=event_choice)

    round_choice = [('preliminary', 'preliminary'), ('final', 'final')]
    round_type = models.CharField(max_length=20, choices=round_choice)

    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        verbose_name = 'Test Timing'
