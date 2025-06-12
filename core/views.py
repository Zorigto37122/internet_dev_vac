from django.views.generic.list import ListView
from django.shortcuts import render
from django.db.models import Q
from core.models import Applicant, Resume, Vacancy


def index(request):
    return render(request,"index.html")

class ApplicantListView(ListView):
    template_name = "applicants.html"
    model = Applicant
    context_object_name = "list_of_all_applicants"

class ResumeListView(ListView):
    template_name = "resumes.html"
    model = Resume
    context_object_name = "list_of_all_resumes"

class SearchView(ListView):
    template_name = "vacancies.html"
    model = Vacancy
    context_object_name = "list_of_all_vacancies"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Vacancy.objects.filter(
                Q(heading__icontains=query) | Q(description__icontains=query) | Q(company__icontains=query) | Q(address__icontains=query)
            )
        return Vacancy.objects.all()


