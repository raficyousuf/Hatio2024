from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    # path('add_todo/', views.add_todo, name='add_todo'),
    path('project/<int:project_pk>/add_todo/', views.add_todo, name='add_todo'),
    path('<int:pk>/edit/', views.edit_todo, name='edit_todo'),
    path('<int:pk>/complete/', views.mark_complete, name='mark_complete'),
    path('add_project/', views.add_project, name='add_project')
]
