from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import CustomUser


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
    
    def get_grade(self):
        grade = 0
        
        for criterion in Criterion.objects.filter(lesson=self):
            grade += criterion.get_total()

        return grade
    
    def __str__(self):
        return self.name + "|" + str(self.user)

class Criterion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, default='', null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    percent = models.IntegerField(
        default=100,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ]
    )

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'
    
    def get_avg_grade(self):
        grades = Grade.objects.filter(criterion=self).values_list('value', flat=True)
        if len(grades):
            avg_grade = sum(grades) / len(grades)
            return round(avg_grade, 3)
        return 0
    
    def get_total(self):
        return round((self.get_avg_grade() * (self.percent / 100)), 3)
    
    def __str__(self):
        return f"{self.name}|{self.lesson.name}|{str(self.lesson.user)}"


class Grade(models.Model):
    value = models.FloatField(
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f"{self.value}|{self.criterion.lesson.user}"
