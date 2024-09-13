from django.db import models
from users.models import CustomUser


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
    
    def __str__(self):
        return self.name + "|" + str(self.user)

class Criterion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    percent = models.IntegerField()

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'
    
    def __str__(self):
        return f"{self.name}|{self.lesson.name}|{str(self.lesson.user)}"


class Grade(models.Model):
    value = models.FloatField()
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f"{self.value}|{self.criterion.lesson.user}"
