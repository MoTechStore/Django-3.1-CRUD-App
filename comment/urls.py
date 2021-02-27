from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
 path('', views.home, name="home"),
 path('motech/', views.motech, name="motech"),
 path('youtube/', views.youtube, name='youtube'),
 path('form/', views.uploadForm, name='form'),
 path('upload/', views.uploadFile, name='upload'),
 path('files/', views.FileView.as_view(), name='files'),
 path('pelcon/', views.PelconView.as_view(), name='pelcon'),
 path('myupload/', views.myUpload, name='myupload'),
 path('pelconUpload/', views.pelconUpload, name='pelconUpload'),
 path('crud/', views.IndexView.as_view(), name='crud'),
 path('student/', views.Student, name='save'),
 path('editdata/', views.editdata, name='edit'),
 path('update/', views.updatedata, name='update'),

 # Appointment Reminder
 path('new/', views.AppointmentCreateView.as_view(), name='new_appointment'),
 path('list/', views.ListStudent.as_view(), name='list'),
 path('add/', views.CreateStudent.as_view(), name='add'),
 path('alist/', views.AppointmentListView.as_view(), name='alist'),
 path('ulist/<int:pk>', views.AppointmentUpdateView.as_view(), name='ulist'),
 path('dlist/<int:pk>', views.AppointmentDeleteView.as_view(), name='dlist'),
 path('vlist/<int:pk>', views.AppointmentDetailView.as_view(), name='vlist'),



# BookApp
path('BookApp/', auth_views.LoginView.as_view(template_name='comment/login.html'), name='login'),
path('add_book/', views.add_book, name='add_book'),
path('listbook/', views.BookListView.as_view(), name='blist'),
path('upload-book/', views.upload_book, name='ubook'),
















]
