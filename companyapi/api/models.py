from django.db import models

# CREATING COMPANY MODEL
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    
    # 1. The choices parenthesis is properly closed below
    type = models.CharField(max_length=100, choices=(
        ('IT', 'IT'),
        ('Non IT', 'Non IT'),
        ('Mobile Phones', 'Mobile Phones')
    )) 
    
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # 2. The __str__ function sits OUTSIDE the field parentheses, indented directly under the class
    def __str__(self):
        return self.name


# CREATING EMPLOYEE MODEL
# 3. This class must be pushed all the way to the left wall (not nested inside Company)
class Employee(models.Model):
    # 4. All these fields must be indented 4 spaces to belong to the Employee class
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    
    # 5. Choices parenthesis properly closed here too
    position = models.CharField(max_length=50, choices=(
        ('Manager', 'Manager'),
        ('Software Developer', 'Software Developer'),
        ('Project Leader', 'Project Leader')
    )) 

    # This is the Relational Link:
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # 6. __str__ function sits properly outside the fields
    def __str__(self):
        return self.name