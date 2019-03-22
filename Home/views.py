from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Home.models import User,Project
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import ProjectForm


from . import urls
from .models import Project


def userSearch(request, nam):
    selist = User.objects.filter(userName=nam)
    output = ', '.join([q.userName for q in selist])

    return HttpResponse(output)


def index(request):
    #latest_question_list = User.objects.order_by('userName')[:2]
    selist = User.objects.filter(userName='abc')
    output = ', '.join([q.userName for q in selist])
    return HttpResponse(output)


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {
        'projects': projects
    })


def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'upload_project.html', {
        'form': form
    })


def delete_project(request, pk):
    if request.method == 'POST':
        project = Project.objects.get(pk=pk)
        project.delete()
    return redirect('project_list')


class ProjectListView(ListView):
    model = Project
    template_name = 'class_project_list.html'
    context_object_name = 'projects'


class UploadProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('class_project_list')
    template_name = 'upload_project.html'
