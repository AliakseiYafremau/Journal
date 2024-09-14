from django.shortcuts import render, redirect

from .forms import *
from .models import *

def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form_type = request.POST.get('form')
        if form_type == 'create':
            form = CreateLessonForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                if Lesson.objects.filter(name=name, user=user).exists():
                    form.add_error('name', 'Lesson already exists')
                else:
                    Lesson.objects.create(name=name, user=user)
        if form_type == 'delete':
            form = DeleteLessonForm(request.POST)
            if form.is_valid():
                id = form.cleaned_data.get('id')
                Lesson.objects.filter(id=id, user=user).delete()
    form = CreateLessonForm()
    
    lessons = Lesson.objects.filter(user=user)
    return render(request,
                  'lessons/home.html',
                  context={'user': request.user, 'form': form, 'lessons': lessons})


def lesson(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    lesson = Lesson.objects.filter(id=id, user=request.user).first()
    if not lesson:
        return redirect('home')
    
    if request.method == 'POST':
        form_type = request.POST.get('form')
        if form_type == 'delete_grade':
            form = DeleteGradeForm(request.POST)
            if form.is_valid():
                id = form.cleaned_data.get('id')
                print(id)
                Grade.objects.filter(id=id).delete()

        if form_type == 'create_grade':
            form = CreateGradeForm(request.POST)
            if form.is_valid():
                value = form.cleaned_data.get('value')
                print(form.cleaned_data)
                criterion = Criterion.objects.filter(id=form.cleaned_data.get('criterion')).first()
                print(criterion)
                Grade.objects.create(value=value, criterion=criterion)

        if form_type == 'delete_criterion':
            form = DeleteCriterionForm(request.POST)
            if form.is_valid():
                id = form.cleaned_data.get('id')
                Criterion.objects.filter(id=id).delete()
        
        if form_type == 'create_criterion':
            form = CreateCriterionForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                description = form.cleaned_data.get('description')
                percent = form.cleaned_data.get('percent')
                lesson = Lesson.objects.filter(id=form.cleaned_data.get('lesson')).first()
                Criterion.objects.create(name=name, description=description, lesson=lesson, percent=percent)
    
    create_grade_form = CreateGradeForm()
    create_criterion_form = CreateCriterionForm()
    
    return render(request, 'lessons/lesson.html',
                  context={'lesson': lesson,
                           'create_grade_form': create_grade_form,
                           'create_criterion_form': create_criterion_form})