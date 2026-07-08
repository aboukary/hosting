from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import StudentForm
from .models import Student


def home(request):
    return render(request, "home.html")


def dashboard(request):

    total_students = Student.objects.count()

    context = {
        "total_students": total_students,
    }

    return render(request, "dashboard.html", context)


class StudentListView(LoginRequiredMixin, ListView):

    model = Student

    template_name = "students/student_list.html"

    context_object_name = "students"

    ordering = ["last_name"]


class StudentCreateView(LoginRequiredMixin, CreateView):

    model = Student

    form_class = StudentForm

    template_name = "students/student_form.html"

    success_url = reverse_lazy("student_list")


class StudentUpdateView(LoginRequiredMixin, UpdateView):

    model = Student

    form_class = StudentForm

    template_name = "students/student_form.html"

    success_url = reverse_lazy("student_list")


class StudentDeleteView(LoginRequiredMixin, DeleteView):

    model = Student

    template_name = "students/student_confirm_delete.html"

    success_url = reverse_lazy("student_list")
