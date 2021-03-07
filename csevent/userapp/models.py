from django.db import models

from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


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
    user_type = models.PositiveSmallIntegerField(choices=user_type_choice)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']


class StudentModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to=models.Q(user_type=3))
    college = models.CharField(max_length=60)
    dept = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=15)
    id_proof = models.ImageField(upload_to="Student_id")
    profile_pic = models.ImageField(upload_to="Student_pic")
    bonafide = models.FileField(upload_to="Student_bonafide")  # optional


# DO WE NEED THIS

# @receiver(post_save, sender=User)
# def create_user_studentmodel(sender, instance, created, **kwargs):
#     if created and instance.user_type == 3:
#         StudentModel.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_studentmodel(sender, instance, **kwargs):
# 	if instance.user_type == 3:
# 		instance.studentmodel.save()
