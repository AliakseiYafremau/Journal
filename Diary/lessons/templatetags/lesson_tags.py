from django import template
from lessons.models import Criterion, Lesson


register = template.Library()

@register.simple_tag
def avg_grade_crit(criterion_id):
    criterion = Criterion.objects.get(id=criterion_id)
    return criterion.get_avg_grade()

@register.simple_tag
def total_grade_crit(criterion_id):
    criterion = Criterion.objects.get(id=criterion_id)
    return criterion.get_total()

@register.simple_tag
def lesson_grade(lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return lesson.get_grade()
