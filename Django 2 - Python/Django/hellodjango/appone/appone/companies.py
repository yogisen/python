from appone.models import Company, Department, Employee

# department creation
dev = Department(name='Development')
dev.save()
design = Department(name='Design')
design.save()
marketing = Department(name='Marketing')
marketing.save()

# Django company creation
django = Company(name='Django')
django.save()

Employee(company=django, department=design, name='John', age=25, salary=3250.20).save()
Employee(company=django, department=dev, name='Alice', age=33, salary=4400.00).save()

# Pear company creation
pear = Company(name='Pear')
pear.save()

Employee(company=pear, department=marketing, name='Jake', age=46, salary=8000.00).save()
Employee(company=pear, department=dev, name='Sarah', age=21, salary=2800.00).save()
