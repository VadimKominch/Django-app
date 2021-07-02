from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.get_employee,name="create"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
]