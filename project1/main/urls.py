from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path('topics/', views.topics_home, name='topics-home'),
    path("create/", views.create, name='create'),
    # path("upload", upload_file, name='file_upload'),
    # path("upload_success", upload_success, name='file_uploaded'),
    # path("upload_failed", upload_fail, name='file_not_uploaded'),

]

