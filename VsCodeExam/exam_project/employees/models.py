from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Employee(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Полное имя')
    position = models.CharField(max_length=100, verbose_name='Должность')
    hire_date = models.DateField(verbose_name='Дата найма')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    email = models.CharField(max_length=100, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.full_name:
            raise ValidationError({"full_name": "Имя не должно быть пустым"})
        if not self.position:
            raise ValidationError({"position": "Позиция не должна быть пустой"})
        if self.hire_date and self.hire_date > datetime.date.today():
            raise ValidationError({"hire_date": "Дата найма не может быть в будущем"})
        if not self.salary or self.salary <= 0:
            raise ValidationError({"salary": "Зарплата должна быть положительной"})
        if Employee.objects.filter(email=self.email).exclude(pk=self.pk).exists() or "@" not in self.email:
            raise ValidationError({"email": "Email должен быть уникален и правильно написан!"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

