from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.pk, self.name)


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.pk, self.name)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '{id} {name}, company={company}, department={department}, age={age}, salary={salary}'.format(
            id=self.pk,
            name=self.name,
            company=self.company,
            department=self.department,
            age=self.age,
            salary=self.salary
        )

