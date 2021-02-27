from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import CustomUserCreationForm
from .models import YouTube, Files, Pelcon,Student, Appointment, Book
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .forms import CustomerForm, StudentForm




account_sid = 'AC46c019ea77dacf86ecea2d4bb44a3ca0'
auth_token = 'eaa7077fa70d51c8397dbb2ee7123ed6'




def home(request):
	like = ['1', '0', '0']
	satisfied = ["Django", "Machine Learning", "Robotics", "None"]
	total_viewer = YouTube.objects.aggregate(Sum("v_watched"))
	print(total_viewer)
	total_viewer = total_viewer.get("v_watched__sum")
	print(total_viewer)


	context = {"like":like, "satisfied":satisfied, "total_viewer":total_viewer}
	return render(request, 'comment/mo.html', context)


def youtube(request):
	if request.method == "POST":
		full_names = request.POST['full_names']
		comment = request.POST['comment']
		v_watched = request.POST['v_watched']
		satisfied = request.POST['satisfied']
		viewer_like = request.POST['viewer_like']
		print("satisfied ? :", satisfied)
		print("Viewer Like : ", viewer_like)

		a = YouTube(full_names=full_names, comment=comment, v_watched=v_watched, satisfied=satisfied, viewer_like=viewer_like)
		a.save()
		messages.success(request, 'Feedback was Submitted successfully!')
		return redirect('home')
	else:
		messages.error(request, 'Failed To Submit Feedback, retry')
		return redirect('home')



def motech(request):
	names = ["Pelcon", "Crow", "Alpine", "Eagle" ]
	context = {"names":names}
	return render(request, 'comment/motech.html', context)



class FileView(generic.ListView):
    model = Files
    template_name = 'comment/file.html'
    context_object_name = 'files'
    paginate_by = 6

    def get_queryset(self):
    	return Files.objects.order_by('-id')



def uploadForm(request):
	return render(request, 'comment/upload.html')


def uploadFile(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        owner = request.POST['owner']
        pdf = request.FILES['pdf']
        cover = request.FILES['cover']

        a = Files(filename=filename, owner=owner, pdf=pdf, cover=cover)
        a.save()
        messages.success(request, 'Files Submitted successfully!')
        return redirect('files')
    else:
    	messages.error(request, 'Files was not Submitted successfully!')
    	return redirect('form')



class PelconView(generic.ListView):
	model = Pelcon
	template_name = 'comment/pelcon.html'
	context_object_name = 'files'
	paginate_by = 4


	def get_queryset(self):
		return Pelcon.objects.order_by('-id')


def myUpload(request):
	return render(request, 'comment/myUpload.html')



def pelconUpload(request):
	if request.method == 'POST':
		name = request.POST['name']
		owner = request.POST['owner']
		pdf = request.FILES['pdf']
		cover = request.FILES['cover']

		a = Pelcon(name=name, owner=owner, pdf=pdf, cover=cover)
		a.save()
		messages.success(request, 'Files was Submitted successfully')
		return redirect('pelcon')
	else:
		messages.error(request, 'Files was not Submitted successfully')
		return redirect('myupload')



class IndexView(generic.ListView):
	model = Pelcon
	template_name = 'comment/home.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Pelcon.objects.order_by('-id')



def myStudent(request):
	if request.method == 'POST':
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		coursename = request.POST['coursename']
		yos = request.POST['yos']


		a = Student(firstname=firstname, lastname=lastname, coursename=coursename, yos=yos)
		a.save()
		messages.success(request, 'Data Was Submitted Successfully')
		return redirect('crud')
	else:
		messages.error(request, 'Data Was Not Submitted Successfully')
		return redirect('crud')


def editdata(request, pk):
	data = get_object_or_404(Student, id=pk)
	alldata = Student.objects.order_by('-id')

	context = {'data': data, 'qid' : pk, 'getdata' : alldata}
	return render(request, 'comment/home.html', context)


def updatedata(request):
		ed = Student.objects.get(id=request.POST['qid'])

		ed.name=request.POST['name']
		ed.question_text=request.POST['questiontext']
		ed.save()



class AppointmentCreateView(SuccessMessageMixin, CreateView):
    model = Appointment
    form_class = CustomerForm
    success_url = reverse_lazy('alist')
    template_name = 'comment/appointment_form.html'
    success_message = 'Appointment successfully created!.'



class CreateStudent(SuccessMessageMixin, CreateView):
    model = Appointment
    form_class = StudentForm
    template_name = 'comment/add_student.html'
    success_url = reverse_lazy('list')
    success_message = 'Student Was Successfully Added!.'


class ListStudent(generic.ListView):
	model = Student
	template_name = 'comment/crud.html'
	context_object_name = 'students'
	paginate_by = 4

	def get_queryset(self):
		return Student.objects.order_by('-id')



# Appointment Reminder

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'comment/appointment_list.html'
    context_object_name = 'apps'
    paginate_by = 4


    def get_queryset(self):
    	return Appointment.objects.order_by('-id')


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'comment/appointment_detail.html'


class AppointmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Appointment
    form_class = CustomerForm
    success_message = 'Appointment successfully updated.'


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'comment/confirm_delete.html'
    success_url = reverse_lazy('alist')


class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'comment/appointment_update.html'
    form_class = CustomerForm
    success_message = 'Success: Data was updated.'
    success_url = reverse_lazy('alist')



def login(request):
	return render(request, 'comment/login.html')



# BookApp Views
def add_book(request):
    return render(request, 'bookapp/add_file.html')


class BookListView(ListView):
    model = Book
    template_name = 'bookapp/book_list.html'
    context_object_name = 'books'
    paginate_by = 4


    def get_queryset(self):
    	return Book.objects.order_by('-id')


def upload_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']
        publisher = request.POST['publisher']
        desc = request.POST['desc']
        cover = request.FILES['cover']
        pdf = request.FILES['pdf']

        a = Book(title=title, author=author, year=year, publisher=publisher,
        	desc=desc, cover=cover, pdf=pdf)
        a.save()
        messages.success = (request, 'Book Uploaded Successfully')
        return redirect('blist')
    else:
        return redirect('add_book')    	