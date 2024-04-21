from django.db import models
from django. contrib.auth.models import AbstractUser

HUMO,UZCARD,VISA='humo','uzcard','visa'

class User(AbstractUser):
    photo=models.ImageField(upload_to='users_photo/', default='users_photo/default.jpeg')
    phone_number=models.CharField(max_length=13,unique=True,null=True,blank=True)

class Card(models.Model):

    CARD_CHOISE_TYPE=(
        (HUMO,HUMO),
        (UZCARD,UZCARD),
        (VISA,VISA),
    )

    card_number=models.CharField(max_length=16, unique=True, db_index=True)
    valid_time=models.CharField(max_length=4)
    card_type=models.CharField(max_length=20, choices=CARD_CHOISE_TYPE)
    bank_name=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cards')

    def __str__(self):
        return f"{self.name}:{self.card_number}"

