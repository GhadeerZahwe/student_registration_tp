# Student Registration Django Project

This is a **Django project** for managing student registration. It demonstrates creating models with **foreign key relationships**, performing CRUD operations, and querying data using the Django ORM.

---

## Project Description

The project manages the following entities:

- **Student** (`S_Id`, `S_name`, `S_DOB`)  
- **Course** (`C_ID`, `C_name`, `C_credits`)  
- **Register** (`S_Id`, `C_ID`, `R_date`)  

**Features:**

- Add, update, delete students, courses, and registrations
- List all students or filter by name
- List all courses
- List all courses for a specific student
- Query students registered after a specific year
- Count students registered before a specific year or in a specific course

---

## Requirements

- Python 3.10+
- Django 4.x
- Virtual Environment (recommended)

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd student_registration
```
2. Create a virtual environment:
```bash
python -m venv venv
```
3. Activate the virtual environment:

Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
4. Install dependencies:
```bash
pip install django
```
---
## Project Setup

1. Navigate to the project folder:
```bash
cd tp2_project
```
2. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Create a superuser for Django admin:
```bash
python manage.py createsuperuser
```
4. Run the development server:
```bash
python manage.py runserver
```
5. Open your browser and go to:
```bash
http://127.0.0.1:8000/admin
```
=> Login with your superuser credentials to manage students, courses, and registrations.

---
## Models
```bash
class Student(models.Model):
    S_name = models.CharField(max_length=100)
    S_DOB = models.DateField()

class Course(models.Model):
    C_name = models.CharField(max_length=100)
    C_credits = models.IntegerField()

class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    R_date = models.DateField()
```

---
#### Example Queries
```bash
from registration.models import Student, Course, Register

# List all students
Student.objects.all()

# List students by name
Student.objects.filter(S_name="Peter")

# List all courses
Course.objects.all()

# Courses related to student "Peter"
Course.objects.filter(register__student__S_name="Peter")

# Students registered after 2024
Register.objects.filter(R_date__year__gt=2024)

# Number of students registered before 2025
Register.objects.filter(R_date__year__lt=2025).count()

# Number of students registered before 2025 in course "DBB"
Register.objects.filter(R_date__year__lt=2025, course__C_name="DBB").count()
```
---


