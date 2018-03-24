from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, FormView, UpdateView, CreateView
from .models import Issue, Tag, User
from .forms import LoginForm


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.user = User.objects.get(username=form.cleaned_data['username'])
        self.request.session['user'] = self.request.user.username
        return super().form_valid(form)


def issueDelete(request, pk=None):
    Issue.objects.delete(pk=pk)
    return HttpResponseRedirect('/')


class IssueCreateView(CreateView):
    model = Issue
    fields = '__all__'
    template_name_suffix = '_add'
    success_url = '/'


class IssueListView(ListView):
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = timezone.now()
        return context


class IssueUpdateView(UpdateView):
    model = Issue
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = '/'


def tag(request):
    if request.method == 'POST':
        # create
        pass
    elif request.method == 'DELETE':
        # delete
        pass

    return HttpResponseRedirect('/')


def userDelete(request, pk=None):
    User.objects.delete(pk=pk)
    return HttpResponseRedirect('/user/')


class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    template_name_suffix = '_add'
    success_url = '/user/'


class UserListView(ListView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'company', 'is_superadmin']

    template_name_suffix = '_update'
