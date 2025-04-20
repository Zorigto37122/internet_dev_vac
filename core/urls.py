from django.urls import path
from .views import index, ApplicantListView, ResumeListView

urlpatterns = [
    path('', index, name="index"),
    path('applicants/', ApplicantListView.as_view(), name='applicants'),
    path('resumes/', ResumeListView.as_view(), name='resumes'),

]