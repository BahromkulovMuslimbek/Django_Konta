from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    photo = models.ImageField(null=True, blank=True)
    instructor = models.CharField(max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.instructor

class Courses(models.Model):
    price = models.FloatField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    describe = models.TextField(null=True, blank=True)
    teacher = models.CharField(max_length=255, null=True, blank=True)
    time = models.FloatField(null=True, blank=True)
    st_quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.teacher

class OurStudentsSay(models.Model):
    photo = models.ImageField(null=True, blank=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)
    profession = models.TextField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.client_name

class CoursesCategories(models.Model):
    photo = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.category