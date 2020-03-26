from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PassForm
from .models import PassModel

# Create your views here.
class PassView(LoginRequiredMixin,ListView):
    model = PassModel
    template_name = "pass/pass_list.html"
    context_object_name = "obj"
    login_url = "login"

    def get_queryset(self):
        queryset = PassModel.objects.all()
        queryset = queryset.filter(user=self.request.user)
        return queryset



class PassCreateView(LoginRequiredMixin,CreateView):
    model = PassModel
    template_name = "pass/pass_form.html"
    context_object_name = "obj"
    form_class = PassForm
    success_url = reverse_lazy("pass_list")
    login_url = "login"

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PassUpdateView(LoginRequiredMixin,UpdateView):
    model = PassModel
    template_name = "pass/pass_form.html"
    context_object_name = "obj"
    form_class = PassForm
    success_url = reverse_lazy("pass_list")
    login_url = "login"

class PassDeleteView(LoginRequiredMixin,DeleteView):
    model = PassModel
    template_name = "pass/pass_del.html"
    context_object_name = "obj"
    form_class = PassForm
    success_url = reverse_lazy("pass_list")
    login_url = "login"