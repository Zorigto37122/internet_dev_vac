from django.db import models

class Applicant(models.Model):
    email = models.EmailField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Resume(models.Model):
    heading = models.CharField(max_length=128)
    description = models.TextField()
    applicant = models.ForeignKey(Applicant, on_delete=models.PROTECT)

    def __str__(self):
        return self.heading

class Vacancy(models.Model):
    heading = models.CharField(max_length=128)
    description = models.TextField()
    salary = models.FloatField()
    number_of_responses = models.IntegerField()
    company = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = 'Vacancies'


