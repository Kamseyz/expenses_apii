from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, RegexValidator
# Create your models here.

User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3, message='Category name must be in the range of 3 -50 characters'), 
                                                       RegexValidator(r'^\S+$', message='Category cannot start with a whitespace')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'This {self.name} category belongs to {self.user}'

class Expense(models.Model):
    title = models.CharField(max_length=100,validators=[MinLengthValidator(3, message='Title must be in the range of 3-100 characters'), 
                                                       RegexValidator(r'^\S+$', message='Title cannot start with a whitespace')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'This user {self.user} made this{self.title} expense with the amount {self.amount} on {self.created_at} date'