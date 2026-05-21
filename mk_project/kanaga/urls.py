from django.urls import path
from.import views

urlpatterns=[
    path('add/',views.add_student,name='add'),
    path('search/',views.search_result,name='search'),
]