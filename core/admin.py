from django.contrib import admin
from .models import Applicant, Resume, Vacancy

admin.site.register(Applicant)
admin.site.register(Resume)
admin.site.register(Vacancy)
