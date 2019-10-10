from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def get(cls, name):
        pass


class Industry(models.Model):
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Questionnaire(models.Model):
    YESNO_CHOICES = (
        ('True', 'True'),
        ('False', 'False')
    )
    submission_date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    sector = models.ManyToManyField(Sector)
    industry = models.ManyToManyField(Industry)
    risk = models.CharField(max_length=5, choices=YESNO_CHOICES)
    csr = models.CharField(max_length=5, choices=YESNO_CHOICES)
    Female_exec = models.CharField(max_length=5, choices=YESNO_CHOICES)
    hr = models.CharField(max_length=5, choices=YESNO_CHOICES)

    def __str__(self):
        return str(self.submission_date)


class Stock(models.Model):
    ticker = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    Female_exec = models.BooleanField()
    risk = models.BooleanField()
    csr = models.BooleanField()
    hr = models.BooleanField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    last_login = models.DateTimeField(default=timezone.now)
    questionnaire = models.ForeignKey(Questionnaire, null=True, on_delete=False)
    user_gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    user_email = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


def create_user_profile(instance, created):
    if created:
        UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


class StockRecommendation(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='stock_recommendations')

    def __str__(self):
        return str(self.stock)