from appone.models import Employee

Employee.objects.filter(company__name='Django')

Employee.objects.filter(company__name='Django', name__startswith='J')

Employee.objects.exclude(department__name='Development').filter(salary__gte=4000.00)

Employee.objects.all().count()

Employee.objects.filter(company__name='Pear').order_by('-age')

from django.db.models import Avg
Employee.objects.filter(company__name='Django').aggregate(Avg('salary'))
