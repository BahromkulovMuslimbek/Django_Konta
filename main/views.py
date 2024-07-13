from django.shortcuts import render, redirect
from . import models

def home(request):
    teachers = models.Teacher.objects.all()
    category = models.CoursesCategories.objects.all()
    print('salom')
    context = {
        'teachers': teachers,
        'category': category
    }
    return render(request, 'index.html', context)

def not_found(request):
    return render(request, 'not_found.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        models.Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
            )

    return render(request, 'contact.html')

def success_view(request):
    return render(request, 'success.html')

def courses(request):
    courses = models.Courses.objects.all()
    return render(request, 'courses.html', {'courses':courses})

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    oss = models.OurStudentsSay.objects.all()
    return render(request, 'testimonial.html', {'oss':oss})