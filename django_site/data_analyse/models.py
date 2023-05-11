from django.db import models


class DataSet(models.Model):
    Win_Field = [
        (1, 'Win'),
        (0, 'Lose')
    ]

    date = models.DateField()
    num_one = models.IntegerField(null=True)
    num_two = models.IntegerField(null=True)
    num_three = models.IntegerField(null=True)
    num_four = models.IntegerField(null=True)
    num_five = models.IntegerField(null=True)
    win = models.BooleanField(choices=Win_Field)
