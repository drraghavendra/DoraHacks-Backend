from django.db import models


# ------------------------------------------------------
# models
# University
# College
# Department
# Course
# Student
# ------------------------------------------------------


# ------------------------------------------------------
class University(models.Model):
    id = models.BigAutoField(primary_key=True)
    uty_name = models.CharField(max_length=255)
    uty_code = models.CharField(max_length=255)

    def __str__(self):
        return self.uty_name


# ------------------------------------------------------
class College(models.Model):
    id = models.BigAutoField(primary_key=True)
    clg_name = models.CharField(max_length=255)
    clg_code = models.CharField(max_length=255)
    uty = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.clg_name


# ------------------------------------------------------
class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=255)
    dept_code = models.CharField(max_length=255)
    clg = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.dept_name


# ------------------------------------------------------
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    uty_regno = models.CharField(max_length=25)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


# ------------------------------------------------------
class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.BigIntegerField(null=True, blank=True)
    grad_level = models.CharField(max_length=1)  # Assuming CHAR(255) should be CHAR(1)

    def __str__(self):
        return self.course_name


# ------------------------------------------------------
