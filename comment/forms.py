from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.forms import ModelForm
from comment.models import Appointment, Student




class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']



class CustomerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['phone_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['time'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['time_zone'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Appointment
        fields = ['name', 'phone_number', 'time', 'time_zone']





class StudentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['lastname'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['coursename'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['yos'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'coursename', 'yos']
