from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, FormView, UpdateView, CreateView
from django.forms.models import modelform_factory
from django.forms import DateTimeInput
from django.db.models import Q, Avg, Max, Min, Count
from .models import Issue, Tag, User
from .forms import LoginForm


def logout(request):
    '''
    Destroy session with user information
    '''
    request.session.flush()
    return HttpResponseRedirect('/')


class AuthView(TemplateView):
    template_name = 'auth.html'


class LoginView(FormView):
    '''
    Show login form
    '''
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        '''
        If user successfully logged
        '''
        self.request.user = User.objects.get(username=form.cleaned_data['username'])
        self.request.session['user'] = self.request.user.username
        return super().form_valid(form)


def issueDelete(request, pk=None):
    '''
    Delete issue
    '''
    Issue.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/')


class IssueAddView(CreateView):
    '''
    Issue creation class
    '''
    model = Issue
    template_name_suffix = '_add'
    success_url = '/'
    fields = ['submitter', 'solver', 'title', 'description', 'state', 'tags']


class IssueListView(ListView):
    '''
    Issue list class
    '''
    model = Issue

    def get_queryset(self):
        '''
        Get queryset filtered by GET args
        '''
        queryset = super(IssueListView, self).get_queryset()

        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tags__id=tag)

        user = self.request.GET.get('user')
        if user:
            queryset = queryset.filter(
                Q(
                    Q(solver_id=user)|Q(submitter_id=user)
                )
            )

        return queryset

    def get_context_data(self, **kwargs):
        '''
        Add data to default listviw
        '''
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['tags'] = Tag.objects.all()
        context['stats'] = self.get_queryset().aggregate(
            Max('duration'),
            Min('duration'),
            Avg('duration'),
        )

        return context


class IssueUpdateView(UpdateView):
    '''
    '''
    model = Issue
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = '/'


class TagListView(ListView):
    '''
    '''
    model = Tag


class TagUpdateView(UpdateView):
    model = Tag
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = '/tag/'


class TagAddView(CreateView):
    model = Tag
    fields = '__all__'
    success_url = '/tag/'
    template_name_suffix = '_add'


def tagDelete(request, pk=None):
    Tag.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/tag/')


class UserAddView(CreateView):
    model = User
    fields = '__all__'
    template_name_suffix = '_add'
    success_url = '/user/'

    def form_valid(self, form):
        # quick hack, there are many method and strategies to solve password managements
        # and do this good way is more difficult than whole app..

        result = super(UserAddView, self).form_valid(form)
        user = User.objects.get(pk=form.instance.pk)
        user.password = User.hashPassword(user.password)
        user.save()
        return result


class UserListView(ListView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'company', 'is_superadmin']
    success_url = '/user/'
    template_name_suffix = '_update'


def userDelete(request, pk=None):
    User.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/user/')
