from django.urls import path 
from . import views

urlpatterns = [
    path('/<str:disease>', views.DiseaseView.as_view(), name="disease"),
    path('/<str:disease>/<str:pathy>', views.TherapyView.as_view(), name="therapy"),
    path('/<str:disease>/<str:pathy>/books', views.BooksView.as_view(), name="books"),
    path('/<str:disease>/<str:pathy>/<str:source>', views.BooksView.as_view(), name="source"),
    path('/<str:disease>/<str:pathy>/direct/<str:case_id>', views.CaseView.as_view(), name="case"),
]