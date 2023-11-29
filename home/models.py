from django.db import models
from django.contrib.auth.models import User
# Create your models here.

expense_type = (
    ('Income', 'Income'),
    ('Expense', 'Expense'),
)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    notes = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=255, choices=expense_type)

    def __str__(self):
        return self.notes + ' | ' + str(self.amount)