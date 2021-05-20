from django.db import models

AccType = (
    ('CA','CA'),
    ('SA','SA')
)


class Account(models.Model):
    name = models.CharField(max_length=200)
    acc_type = models.CharField(max_length=2, choices=AccType, default='SA')
    balance = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
