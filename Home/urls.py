from django.urls import path


from . import views
urlpatterns = [
    path('user_search/<slug:nam>/', views.userSearch, name='userSearch'),
    path('upload_project/',views.upload_project),
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('projects/', views.project_list, name="project_list"),
    path('projects/upload/', views.upload_project, name='upload_project'),
    path('projects/<int:pk>/', views.delete_project, name='delete_project'),

    path('class/projects/', views.ProjectListView.as_view(), name='class_project_list'),
    path('class/projects/upload/', views.UploadProjectView.as_view(),
         name='class_upload_project'),
    

   # path('', views.index),
]
