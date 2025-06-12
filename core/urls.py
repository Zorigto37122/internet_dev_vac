from django.urls import path, include
from .views import index, ApplicantListView, ResumeListView, SearchView

urlpatterns = [
    path('', index, name="index"),
    path('applicants/', ApplicantListView.as_view(), name='applicants'),
    path('resumes/', ResumeListView.as_view(), name='resumes'),
    path('vacancies/', SearchView.as_view(), name='vacancies'),
    path('accounts/', include('django.contrib.auth.urls')),
]